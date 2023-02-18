from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("template_python_test_repo")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version
