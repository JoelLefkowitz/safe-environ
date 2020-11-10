class MissingEnvVar(Exception):
    def __init__(self, env_var_name: str) -> None:
        super().__init__(f"The environment variable '{env_var_name}' is not set")


class InvalidEnvVar(Exception):
    def __init__(self, env_var_name: str) -> None:
        super().__init__(f"The environment variable '{env_var_name}' is empty or None")
