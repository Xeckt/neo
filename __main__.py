import discord
from discord.ext import commands

import handler.config.data
import handler.logging.bot_log
import settings.constants

bot_data = handler.config.data.BotData()


class Foxcord(discord.Client):
    constants = settings.constants
    bot_log = handler.logging.bot_log.BotLog()
    log = bot_log.setup_log(__name__, constants.BOT_LOG_PATH)

    async def on_ready(self):
        print(f"[BOT] -> {self.user} connected to guild {discord.utils.get(self.guilds)}")

    async def on_message(self, ctx, error):
        pass

    def prepare_bot(self):
        bot_data.read_bot_config()


if __name__ == "__main__":
    Foxcord().prepare_bot()
    Foxcord().run(bot_data.get_token())
