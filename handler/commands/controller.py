from handler.config.data import Data
import os


class FoxcordCommands:
    data = Data()
    total_loaded = 0

    def __init__(self, bot):
        self.bot = bot

    def load(self):
        if self.data.dev_commands:
            self.set_command_state(self.data.dev_cog, 'load')
        if self.data.admin_commands:
            self.set_command_state(self.data.admin_cog, 'load')
        if self.data.mod_commands:
            self.set_command_state(self.data.mod_cog, 'load')
        if self.data.user_commands:
            self.set_command_state(self.data.user_cog, 'load')

    def set_command_state(self, module, state, command=None):
        path_string = self.data.cog_path + '.' + module
        if command and isinstance(command, str):
            arg = {path_string + '.' + command}
            getattr(self.bot, "%s_extension" % state)(*arg)
        else:
            for cmd in os.listdir(self.data.cog_path.replace('.', '/') + '/' + module):
                if cmd.endswith('.py'):
                    arg = {path_string + '.' + cmd[:-3]}
                    getattr(self.bot, "%s_extension" % state)(*arg)
                    self.total_loaded += 1
