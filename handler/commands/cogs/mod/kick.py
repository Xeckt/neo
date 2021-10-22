import discord
import handler.config.data
from discord.ext import commands


class Kick(commands.Cog):

    bot_data = handler.config.data.FoxcordData()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(description="Ping bot")
    @commands.has_any_role(bot_data.mod_id, bot_data.admin_id)
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
