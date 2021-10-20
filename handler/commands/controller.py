import settings.constants
import handler.logging.foxlog
import handler.config.data
import os


class FoxcordCommands:
    constants = settings.constants

    user_commands_loaded = 0
    mod_commands_loaded = 0
    admin_commands_loaded = 0
    total_commands_loaded = 0

    command_log = handler.logging.foxlog.BotLog().setup_log(__name__, constants.COMMANDS_LOG_PATH)

    def load(self):
        if self.constants.ENABLE_USER_COMMANDS:
            self.load_user_commands()
            self.command_log.info("User commands loaded -> " + str(self.user_commands_loaded))
        else:
            self.command_log.info("User commands not enabled or loaded.")
        if self.constants.ENABLE_MOD_COMMANDS:
            self.load_mod_commands()
            self.command_log.info("Moderator commands loaded -> " + str(self.mod_commands_loaded))
        else:
            self.command_log.info("Moderator commands not enabled or loaded.")
        if self.constants.ENABLE_ADMIN_COMMANDS:
            self.load_admin_commands()
            self.command_log.info("Administrator commands loaded -> " + str(self.admin_commands_loaded))
        else:
            self.command_log.info("Administrator commands not enabled or loaded.")
        self.total_commands_loaded = self.user_commands_loaded + self.mod_commands_loaded + self.admin_commands_loaded
        self.command_log.info("Total commands loaded -> " + str(self.total_commands_loaded))

    def __init__(self, bot):
        self.bot = bot

    def load_user_commands(self):
        for cog in os.listdir(self.constants.COGS_USER.replace(".", "/")):
            if cog.endswith('.py'):
                self.bot.load_extension(f"{self.constants.COGS_USER + '.' + cog[:-3]}")
                self.user_commands_loaded += 1

    def load_mod_commands(self):
        for cog in os.listdir(self.constants.COGS_MOD.replace(".", "/")):
            if cog.endswith('.py'):
                self.bot.load_extension(f"{self.constants.COGS_MOD + '.' + cog[:-3]}")
                self.mod_commands_loaded += 1

    def load_admin_commands(self):
        for cog in os.listdir(self.constants.COGS_ADMIN.replace(".", "/")):
            if cog.endswith('.py'):
                self.bot.load_extension(f"{self.constants.COGS_ADMIN + '.' + cog[:-3]}")
                self.admin_commands_loaded += 1

    def load_command(self, command_rank, command):
        match command_rank.lower():
            case "user":
                self.bot.load_extension(f"{self.constants.COGS_USER + '.' + command.lower()}")
            case "mod":
                self.bot.load_extension(f"{self.constants.COGS_MOD + '.' + command.lower()}")
            case "admin":
                self.bot.load_extension(f"{self.constants.COGS_ADMIN + '.' + command.lower()}")

    def reload_command(self, command_rank, command):
        match command_rank.lower():
            case "user":
                self.bot.reload_extension(f"{self.constants.COGS_USER + '.' + command.lower()}")
            case "mod":
                self.bot.reload_extension(f"{self.constants.COGS_MOD + '.' + command.lower()}")
            case "admin":
                self.bot.reload_extension(f"{self.constants.COGS_ADMIN + '.' + command.lower()}")

    def unload_command(self, command_rank, command):
        match command_rank.lower():
            case "user":
                self.bot.unload_extension(f"{self.constants.COGS_USER + '.' + command.lower()}")
            case "mod":
                self.bot.unload_extension(f"{self.constants.COGS_MOD + '.' + command.lower()}")
            case "admin":
                self.bot.unload_extension(f"{self.constants.COGS_ADMIN + '.' + command.lower()}")
