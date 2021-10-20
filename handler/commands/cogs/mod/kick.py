import discord
import handler.logging.foxlog
from discord.ext import commands
import settings.constants as constants

class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.is_owner()
    @commands.command(description="Ping bot")
    @commands.has_any_role(constants.MOD_ROLE_ID)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def kick(self, ctx, user: discord.User):
        try:
            await ctx.guild.kick(user=user)
            await ctx.channel.send(f"{user} has been kicked by: {ctx.author.mention}")
        except (discord.ext.commands.UserInputError, discord.ext.commands.UserNotFound) as err:
            await ctx.channel.send(f"{ctx.author.mention}, you need to specify the user to kick!")
            return


def setup(bot):
    bot.add_cog(Kick(bot))
