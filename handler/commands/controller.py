import settings.constants
import handler.logging.bot_log
import handler.config.data
import os


class FoxcordCommands:

    constants = settings.constants
    commands_loaded = 0
    command_log = handler.logging.bot_log.BotLog().setup_log(__name__, constants.COMMANDS_LOG_PATH)

    def __init__(self, bot):
        self.bot = bot

    def load_user_commands(self):
        self.command_log.info("Loading user commands")
        for cog in os.listdir(self.constants.COGS_USER_PATH):
            if cog.endswith(".py"):
                self.bot.load_extension(f"{self.constants.COGS_USER_PATH.replace('/', '.') + '.' + cog[:-3]}")
                self.commands_loaded += 1
