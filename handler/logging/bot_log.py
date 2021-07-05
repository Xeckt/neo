import logging
import sys


class BotLog:

    bot_log_path = "logs/bot.log"
    commands_log_path = "logs/commands.log"
    system_log_path = "logs/system.log"
    log_format = logging.Formatter("%(asctime)s | Module: %(name)s | %(levelname)s | %(message)s")

    def setup_log(self, name, log_file, level=logging.INFO):
        log_file_handler = logging.FileHandler(log_file)
        log_file_handler.setFormatter(self.log_format)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.log_format)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(log_file_handler)
        logger.addHandler(console_handler)
        return logger

