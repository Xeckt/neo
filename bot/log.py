import logging
import globals
from logging.handlers import TimedRotatingFileHandler


class Log:

    formatter = "%(asctime)s | Module: %(name)s | %(levelname)s | %(message)s"

    def create(self, name, log_file):
        level = 0

        match globals.neo_config.logMode:
            case "info":
                level = logging.INFO
            case "debug":
                level = logging.DEBUG
            case "warn":
                level = logging.WARNING
            case "error":
                level = logging.ERROR

        # handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(CustomFormatter(self.formatter))

        logger = logging.getLogger(name)
        logger.setLevel(level)

        # handler for file output, only when "enabledLogging" is true in the yaml config
        if globals.neo_config.enableLogging:
            rotate_handler = TimedRotatingFileHandler(filename=log_file, when='h', interval=1, backupCount=2)
            rotate_handler.setFormatter(logging.Formatter(self.formatter))
            logger.addHandler(rotate_handler)

        logger.addHandler(console_handler)

        return logger

class CustomFormatter(logging.Formatter):
    """
    Logging colored formatter
    https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging/
    """

    grey = '\x1b[38;21m'
    orange = '\x1b[38;5;208m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.orange + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)