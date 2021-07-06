import handler.config.data
import handler.logging.bot_log
import handler.commands.controller
import settings.constants
import discord
from discord.ext import commands

bot_data = handler.config.data.BotData()
bot_data.read_bot_config()

class Foxcord:

    constants = settings.constants
    bot_log = handler.logging.bot_log.BotLog().setup_log(__name__, constants.BOT_LOG_PATH)
    command_log = handler.logging.bot_log.BotLog().setup_log("COMMANDS", constants.COMMANDS_LOG_PATH)
    foxcord = commands.Bot(command_prefix=bot_data.get_prefix())

    async def on_ready(self):
        self.bot_log.info(f"[BOT] -> {self.foxcord.user} connected to guild {discord.utils.get(self.foxcord.guilds)}")

    async def on_message(self, ctx):
        pass

    async def on_command(self, ctx):
        self.command_log.info(f"Command invoked by {ctx.author}: {ctx.command}")

    def init(self):
        self.load_commands()
        self.foxcord.run(bot_data.get_token())

    def load_commands(self):
        commands = handler.commands.controller.FoxcordCommands(self.foxcord)
        commands.load_user_commands()
        commands.load_mod_commands()
        commands.load_admin_commands()
        self.bot_log.info(f"Commands loaded: {commands.amount_loaded}")


if __name__ == "__main__":
    Foxcord().init()
