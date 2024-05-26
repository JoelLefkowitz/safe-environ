import os
from .exceptions import MissingEnvVar


def from_env(name: str) -> str:
    if name not in os.environ:
        raise MissingEnvVar(name)

    return os.environ[name]
