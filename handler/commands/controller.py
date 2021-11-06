import string
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
            self.set_command_state(self.bot_data.dev_cog, 'load')
        if self.bot_data.admin_commands:
            self.set_command_state(self.bot_data.admin_cog, 'load')
        if self.bot_data.mod_commands:
            self.set_command_state(self.bot_data.mod_cog, 'load')
        if self.bot_data.user_commands:
            self.set_command_state(self.bot_data.user_cog, 'load')

    def set_command_state(self, module, state, command=None):
        path_string = self.bot_data.cog_path + '.' + module
        if command and isinstance(command, str):
            arg = {path_string + '.' + command}
            getattr(self.bot, "%s_extension" % state)(*arg)
        else:
            for cmd in os.listdir(self.bot_data.cog_path.replace('.', '/') + '/' + module):
                if cmd.endswith('.py'):
                    arg = {path_string + '.' + cmd[:-3]}
                    getattr(self.bot, "%s_extension" % state)(*arg)
                    self.total_loaded += 1
