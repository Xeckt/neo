from builtins import Exception


class TokenNotFound(Exception):
    def __init__(self, function):
        self.function = function

    def __str__(self):
        return f"Token not found in .env, .yml files or host environment variables."


class SqlHostConnectionError(Exception):
    def __init__(self, function, host):
        self.function = function
        self.host = host

    def __str__(self):
        return f"{self.host} inside function {self.function} cannot be pinged or is invalid."


class InvalidYamlConfig(Exception):
    def __init__(self, config, err):
        self.config = config
        self.err = err

    def __str__(self):
        return f"{self.config} is invalid. Parser returned error -> {self.err}"