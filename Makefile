SOURCE_FILES = Makefile cookiecutter.json {{cookiecutter.project_name}}/* {{cookiecutter.project_name}}/*/*
GENERATED_PROJECT := template_python_test_repo

ENV := .venv

# disable less in gh
PAGER=
export PAGER

# disable commands output
.SILENT:

.PHONY: all
all: install

.PHONY: doctor
doctor:  ## Confirm system dependencies are available
	{{cookiecutter.project_name}}/bin/verchew

# MAIN ########################################################################

.PHONY: ci
ci:
	$(MAKE) ci-cleanup

	poetry run cookiecutter . --no-input --overwrite-if-exists github_repo=$(GENERATED_PROJECT)
	git config --global user.email "you@example.com"
	git config --global user.name "Your Name"
  	make -C $(GENERATED_PROJECT) repo-init
	$(MAKE) ci-wait-complete
	$(MAKE) ci-check-conclusion

	$(MAKE) ci-cleanup

ci-check-conclusion:
	cd $(GENERATED_PROJECT) && \
	CONCLUSION=$$(gh run list --json conclusion -q '.[0].conclusion') && \
	echo "$(GENERATED_PROJECT) ci completed with status: $$CONCLUSION" && \
	if [[ $$CONCLUSION != "success" ]]; then \
		echo "FAIL"; \
		exit 1; \
	else \
		echo "PASS"; \
	fi

ci-wait-complete:
	cd $(GENERATED_PROJECT) && \
	echo "Waiting for $(GENERATED_PROJECT) ci to complete..." && \
	while True; do \
		gh run list --json status,conclusion; \
		if [[ "$$(gh run list --json status -q '.[0].status')" == "completed" ]]; then \
			break; \
		fi \
	done

ci-cleanup:
	# remove project dir if left
	rm -rf $(GENERATED_PROJECT) ; gh repo delete $(GENERATED_PROJECT) --confirm; true
	# remove project repo if left


.PHONY: dev
dev: install clean
	poetry run sniffer

# DEPENDENCIES ################################################################

.PHONY: install
install: $(ENV)
$(ENV): poetry.lock
	@ poetry config virtualenvs.in-project true
ifdef CI
	poetry install --no-dev
else
	poetry install
endif
	@ touch $@

ifndef CI
poetry.lock: pyproject.toml
	poetry lock --no-update
	@ touch $@
endif

# BUILD #######################################################################

.PHONY: build
build: install $(GENERATED_PROJECT)
$(GENERATED_PROJECT): $(SOURCE_FILES)
	cat cookiecutter.json
	poetry run cookiecutter . --no-input --overwrite-if-exists
ifndef CI
endif
	cd $(GENERATED_PROJECT) && poetry lock --no-update
	@ touch $(GENERATED_PROJECT)

# CLEANUP #####################################################################

.PHONY: clean
clean:
	rm -rf $(GENERATED_PROJECT)

.PHONY: clean-all
clean-all: clean
	rm -rf $(ENV)
