import discord
from discord.ext import commands

import handler.config.data
import handler.logging.bot_log
import settings.constants


class Foxcord:

    foxcord = commands.Bot(command_prefix=None)

    def __init__(self):
        self.init_bot_data()
        self.constants = settings.constants
        self.bot_data = handler.config.data.BotData
        self.bot_log = handler.logging.bot_log.BotLog()
        self.log = self.bot_log.setup_log(__name__, self.constants.BOT_LOG_PATH)

    def run_foxcord(self):
        self.foxcord.command_prefix(self.bot_data().get_bot_prefix())
        pass

    def init_bot_data(self):
        self.bot_data().read_bot_config()
        pass

    @foxcord.event
    async def on_ready(self):
        self.log.info(f"[BOT] -> {self.foxcord.user}connected to guild {discord.utils.get(self.foxcord.guilds)}")
        pass

    @foxcord.event
    async def on_message(self, ctx, error):
        pass


if __name__ == "__main__":
    Foxcord().__init__()
    Foxcord().init_bot_data()
    Foxcord().run_foxcord()
