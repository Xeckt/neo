import discord
from discord.ext import commands

import handler.config.data
import settings.constants

constants = settings.constants
bot_data = handler.config.data.BotData()

foxcord = commands.Bot(command_prefix=None)


def run_foxcord():
    bot_data.read_bot_config()
    foxcord.command_prefix(bot_data.get_bot_prefix())
    pass


@foxcord.event
async def on_ready():
    pass


@foxcord.event
async def on_message(ctx, error):
    pass
