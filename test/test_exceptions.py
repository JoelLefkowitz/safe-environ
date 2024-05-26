import os
import pytest
from src.environ import from_env
from src.exceptions import MissingEnvVar


def test_missing_env_var() -> None:
    if "TEST" in os.environ.keys():
        os.environ.pop("TEST")

    with pytest.raises(MissingEnvVar) as error:
        from_env("TEST")

    assert str(error.value) == "The environment variable 'TEST' is not set"
