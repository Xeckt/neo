import os
from config.neoconfig import NeoConfig
from logger.log import Log

class CommandController:
    data = NeoConfig()
    command_log = Log().create(__name__, data.commandLog)

    cog_path = "commands"
    total_loaded = 0

    STATE_LOAD = "load"
    STATE_RELOAD = "reload"
    STATE_UNLOAD = "unload"

    def __init__(self, bot):
        self.bot = bot

    def load_cmds(self):
        self.command_log.info("Loading command cogs")
        self.set_cog_state("dev", self.STATE_LOAD)
        self.set_cog_state("admin", self.STATE_LOAD)
        self.set_cog_state("mod", self.STATE_LOAD)
        self.set_cog_state("user", self.STATE_LOAD)
        self.command_log.info(f"Total commands loaded: {self.total_loaded}")

    def set_cog_state(self, cog, state):
        path_string = self.cog_path + '.' + cog

        for cmd in os.listdir(path_string.replace('.', os.path.sep)):

            if cmd.endswith('.py') and cmd != "__init__.py":

                getattr(self.bot, "%s_extension" % state)(*{path_string + f".{cmd[:-3]}"})
                self.command_log.debug(f"Set %s command %s state to %s", cog, cmd[:-3], state)

                if state == self.STATE_LOAD:
                    self.total_loaded += 1

                elif state == self.STATE_UNLOAD:
                    self.total_loaded -= 1

    def set_command_state(self, cog, state, command: str):
        cog = self.cog_path + '.' + cog

        for cmd in os.listdir(cog.replace('.', os.path.sep)):

            if cmd != "__init__.py" and cmd == command:

                getattr(self.bot, "%s_extension" % state)(*{cog + f".{command[:-3]}"})

                self.command_log.debug(f"Set %s command %s state to %s", cog, command[:-3], state)

                if state == self.STATE_LOAD:
                    self.total_loaded += 1

                elif state == self.STATE_UNLOAD:
                    self.total_loaded -= 1
