import handler.config.data
import handler.logging.foxlog
import os


class FoxcordCommands:
    bot_data = handler.config.data.FoxcordData()

    total_loaded = 0

    def __init__(self, bot):
        self.bot = bot

    def load(self):
        if self.bot_data.dev_commands:
            self.set_module('dev', 'load')
        if self.bot_data.admin_commands:
            self.set_module('admin', 'load')
        if self.bot_data.mod_commands:
            self.set_module('mod', 'load')
        if self.bot_data.user_commands:
            self.set_module('user', 'load')

    def set_module(self, module, state):
        for cog in os.listdir(self.bot_data.cog_path.replace('.', '/') + '/' + module):
            if cog.endswith('.py'):
                match state:
                    case "load":
                        self.bot.load_extension(f"{self.bot_data.cog_path + '.' + module + '.' + cog[:-3]}")
                        self.total_loaded += 1
                    case "reload":
                        self.bot.reload_extension(f"{self.bot_data.cog_path + '.' + module + '.' + cog[:-3]}")
                    case "unload":
                        self.bot.unload_extension(f"{self.bot_data.cog_path + '.' + module + '.' + cog[:-3]}")

    def set_command(self, module, state, command):
        match state:
            case "load":
                self.bot.load_extension(f"{self.bot_data.cog_path + '.' + module + '.' + command}")
            case "reload":
                self.bot.reload_extension(f"{self.bot_data.cog_path + '.' + module + '.' + command}")
            case "unload":
                self.bot.unload_extension(f"{self.bot_data.cog_path + '.' + module + '.' + command}")