import handler.config.data
import handler.logging.foxlog
import handler.commands.controller
import settings.constants
import discord
from discord.ext import commands

bot_data = handler.config.data.BotData()
bot_data.read_bot_config()

class Foxcord:

    constants = settings.constants
    bot_log = handler.logging.foxlog.BotLog().setup_log(__name__, constants.BOT_LOG_PATH)
    command_log = handler.logging.foxlog.BotLog().setup_log("COMMANDS", constants.COMMANDS_LOG_PATH)
    foxcord = commands.Bot(command_prefix=bot_data.get_prefix())

    async def on_ready(self):
        self.bot_log.info(f"[BOT] -> {self.foxcord.user} connected to guild {discord.utils.get(self.foxcord.guilds)}")

    async def on_message(self, ctx):
        pass

    async def on_command(self, ctx):
        self.command_log.info(f"Command invoked by {ctx.author}: {ctx.command}")

    def init(self):
        commands = handler.commands.controller.FoxcordCommands(self.foxcord)
        commands.load()
        self.bot_log.info(f"Commands loaded: {commands.amount_loaded}")
        self.foxcord.run(bot_data.get_token())



if __name__ == "__main__":
    Foxcord().init()
