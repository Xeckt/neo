from discord.ext import commands
import settings.constants as constants


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(description="Ping bot")
    @commands.has_any_role(constants.USER_ROLE_ID)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))
