from disnake.ext import commands
from handler.config.data import Data


class Ping(commands.Cog):

    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(description="Ping bot")
    @commands.has_any_role(
        data.config["memberRoleId"]
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def ping(self, inter):
        await inter.send("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))
