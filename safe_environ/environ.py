import os
from typing import Any

from .exceptions import InvalidEnvVar, MissingEnvVar


def from_env(name: str) -> Any:
    if name not in os.environ:
        raise MissingEnvVar(name)

    value = os.environ.get(name)
    if value == None:
        raise InvalidEnvVar(name)

    return value
