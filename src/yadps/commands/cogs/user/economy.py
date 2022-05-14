import requests
import disnake
import asyncio
from disnake.ext import commands
from yadps.config.data import Data
from yadps.database.sql import Sql

class Economy(commands.Cog):

    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        pass

def setup(bot):
    bot.add_cog(Economy(bot))
