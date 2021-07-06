import settings.constants
import handler.logging.bot_log
import handler.config.data
import os


class FoxcordCommands:

    constants = settings.constants
    amount_loaded = 0
    command_log = handler.logging.bot_log.BotLog().setup_log(__name__, constants.COMMANDS_LOG_PATH)

    def __init__(self, bot):
        self.bot = bot

    def load_user_commands(self):
        self.command_log.info("Loading user commands")
        for cog in os.listdir(self.constants.COGS_USER_PATH):
            if cog.endswith(".py"):
                self.bot.load_extension(f"{self.constants.COGS_USER_PATH.replace('/', '.') + '.' + cog[:-3]}")
                self.amount_loaded += 1

    def load_mod_commands(self):
        self.command_log.info("Loading mod commands")
        for cog in os.listdir(self.constants.COGS_MOD_PATH):
            if cog.endswith(".py"):
                self.bot.load_extension(f"{self.constants.COGS_MOD_PATH.replace('/', '.') + '.' + cog[:-3]}")
                self.amount_loaded += 1

    def load_admin_commands(self):
        self.command_log.info("Loading admin commands")
        for cog in os.listdir(self.constants.COGS_ADMIN_PATH):
            if cog.endswith(".py"):
                self.bot.load_extension(f"{self.constants.COGS_ADMIN_PATH.replace('/', '.') + '.' + cog[:-3]}")
                self.amount_loaded += 1