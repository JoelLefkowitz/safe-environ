import os
from src.environ import from_env


def test_from_env() -> None:
    os.environ["TEST"] = "a"
    assert from_env("TEST") == "a"
