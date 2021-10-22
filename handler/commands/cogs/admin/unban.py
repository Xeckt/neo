import handler.logging.foxlog
import handler.config.data
from discord.ext import commands


class Unban(commands.Cog):

    bot_data = handler.config.data.FoxcordData()
    foxlog = handler.logging.foxlog.Log().setup_log(__name__, bot_data.log)


    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(
        description="Unban a given user.",
        hidden=True
    )
    @commands.has_any_role(
        bot_data.admin_id
    )
    async def unban(self, ctx, userid):
        user = await self.bot.fetch_user(userid)
        await ctx.guild.unban(user)
        self.foxlog.warning(f"{user} has been unbanned!")
        await ctx.send(f"{user} is now unbanned.")


def setup(bot):
    bot.add_cog(Unban(bot))
