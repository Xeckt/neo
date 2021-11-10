import discord
import handler.config.data
import handler.logging.foxlog
from discord.ext import commands


class Ban(commands.Cog):

    bot_data = handler.config.data.FoxcordData()
    foxlog = handler.logging.foxlog.Log().create_logger(__name__, bot_data.log)

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(
        description="Ban a given user.",
        hidden=True
    )
    @commands.has_any_role(
        bot_data.admin_id
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
