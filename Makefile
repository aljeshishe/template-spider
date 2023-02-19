SOURCE_FILES = Makefile cookiecutter.json {{cookiecutter.project_name}}/* {{cookiecutter.project_name}}/*/*
GENERATED_PROJECT := template_spider_test_repo

SHELL := /bin/bash

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

.PHONY: github-ci
github-ci:
	$(MAKE) ci-cleanup

	poetry run cookiecutter . --no-input --overwrite-if-exists github_repo=$(GENERATED_PROJECT)
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
	while true; do \
		RESULT=$$(gh run list --json status,conclusion); \
		STATUS=$$(echo "$$RESULT" | jq -r '.[0].status'); \
		CONCLUSION=$$(echo "$$RESULT" | jq -r '.[0].conclusion'); \
		echo status=$$STATUS conclusion=$$CONCLUSION; \
		if [[ "$$STATUS" == "completed" ]]; then \
			break; \
		fi; \
		sleep 5; \
	done;

ci-cleanup:
	# remove project repo if left
	gh repo view  $(GENERATED_PROJECT) > /dev/null 2>&1 && gh repo delete $(GENERATED_PROJECT) --confirm || true
	# remove project dir if left
	[ -d "$(GENERATED_PROJECT)" ] && rm -rf $(GENERATED_PROJECT)  || true


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
build: install
	cat cookiecutter.json
	poetry run cookiecutter . --no-input --overwrite-if-exists github_repo=$(GENERATED_PROJECT)

# $(GENERATED_PROJECT): $(SOURCE_FILES)
$(GENERATED_PROJECT):
#ifndef CI
#endif
#	cd $(GENERATED_PROJECT) && poetry lock --no-update
#	@ touch $(GENERATED_PROJECT)

# CLEANUP #####################################################################

.PHONY: clean
clean:
	rm -rf $(GENERATED_PROJECT)

.PHONY: clean-all
clean-all: clean
	rm -rf $(ENV)

template-ci:
	$(MAKE) -C $(GENERATED_PROJECT) ci

bake:
	 # remove everything but .env (because it's slow to recreate
	 [[ -d $(GENERATED_PROJECT) ]] && mv $(GENERATED_PROJECT)/.venv .venv_backup && \
	 	rm -rf $(GENERATED_PROJECT)/* && \
	 	mv .venv_backup $(GENERATED_PROJECT)/.venv || true
	poetry run cookiecutter . --no-input --overwrite-if-exists github_repo=$(GENERATED_PROJECT)
	cd $(GENERATED_PROJECT) && \
		git config --global user.email "you@example.com"  && \
		git config --global user.name "Your Name"  && \
  		rm -rf .git && git init && git add . && git commit -m initial

unbake:
	cd $(GENERATED_PROJECT) && git diff --cached > ../patch
	sed 's/$(GENERATED_PROJECT)/{{cookiecutter.package_name}}/g' patch  > patch_fixed
	git apply patch_fixed --index --directory \{\{cookiecutter.project_name\}\}

