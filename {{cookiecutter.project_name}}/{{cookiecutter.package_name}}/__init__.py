from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{cookiecutter.package_name}}")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version
