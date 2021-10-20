import discord
import settings.constants as constants
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.is_owner()
    @commands.command(
        description="Ban a given user.",
        hidden=True
    )
    @commands.has_any_role(constants.ADMIN_ROLE_ID)
    async def ban(self, ctx, user: discord.User):
        if user == ctx.message.author:
            await ctx.send(f"You can't ban yourself, {ctx.message.author.name}")
            return
        await ctx.guild.ban(user)
        await ctx.send(f"{ctx.author.mention} has banned {user}")


def setup(bot):
    bot.add_cog(Ban(bot))
