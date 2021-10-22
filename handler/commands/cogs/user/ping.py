from discord.ext import commands
import handler.config.data


class Ping(commands.Cog):

    bot_data = handler.config.data.FoxcordData()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(description="Ping bot")
    @commands.has_any_role(
        bot_data.user_id,
        bot_data.mod_id,
        bot_data.admin_id,
        bot_data.dev_id
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def ping(self, ctx):
        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))
