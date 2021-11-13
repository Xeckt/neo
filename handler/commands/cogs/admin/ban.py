from handler.config.data import Data
from handler.logging.log import Log
from disnake.ext import commands
import disnake as discord


class Ban(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot
        self.foxlog = Log().create(__name__, self.data.bot_log)

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Ban a given user.",
        hidden=True
    )
    @commands.has_any_role(
        data.admin_id
    )
    async def ban(self, ctx, user: discord.User):
        if user == ctx.message.author:
            await ctx.send(f"You can't ban yourself, {ctx.message.author.mention}")
            return
        await ctx.guild.ban(user)
        self.foxlog.warning(f"{user} has been banned!")
        await ctx.send(f"{ctx.message.author.mention} gave the banhammer to {user}")


def setup(bot):
    bot.add_cog(Ban(bot))
