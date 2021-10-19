import settings.constants
import handler.logging.foxlog
import handler.config.data
import os


class FoxcordCommands:

    constants = settings.constants
    amount_loaded = 0
    command_log = handler.logging.foxlog.BotLog().setup_log(__name__, constants.COMMANDS_LOG_PATH)


    def load(self):
        if self.constants.ENABLE_USER_COMMANDS:
            self.load_user_commands()
            self.command_log.info("User commands loaded")
        else:
            self.command_log.info("User commands not enabled or loaded.")
        if self.constants.ENABLE_MOD_COMMANDS:
            self.load_mod_commands()
            self.command_log.info("Moderator commands loaded")
        else:
            self.command_log.info("Moderator commands not enabled or loaded.")
        if self.constants.ENABLE_ADMIN_COMMANDS:
            self.load_admin_commands()
            self.command_log.info("Administrator commands loaded")
        else:
            self.command_log.info("Administrator commands not enabled or loaded.")

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