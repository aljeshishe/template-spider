# Jace's Python Template

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template basaed in [template-python](https://github.com/aljeshishe/template-python)

## Requirements
[asdf](https://asdf-vm.com/guide/getting-started.html)

## Usage

Install `cookiecutter` and generate a project:

```
pip install cookiecutter
cookiecutter gh:aljeshishe/template-scrapy
```

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.
To generate project without asking questions, use the following command:

```
cookiecutter gh:aljeshishe/template-scrapy --no-input project_name=<project_name>
```

Once created, run the code formatter to updates files based on your chosen names:

```
cd <project_name>
make repo-init      # create repo and push to git
asdf install        # install all necessary tools
poetry run          # install third party dependencies and run
```

## Updates

Run the update tool, which is generated inside each project:

```
$ bin/update
```

## Development
1. Render template to template_spider_test_repo
```
make bake
```
2. Make some changes in template_spider_test_repo
3. Copy changes back to template
```
make unbake
```
