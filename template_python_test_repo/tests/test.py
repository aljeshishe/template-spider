"""Sample integration test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

import pytest
from click.testing import CliRunner
from expecter import expect

from template_python_test_repo.cli import main


def test():
    assert True
