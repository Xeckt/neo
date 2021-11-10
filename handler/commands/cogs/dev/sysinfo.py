from discord.ext import commands
import handler.config.data
import platform

class SysInfo(commands.Cog):

    bot_data = handler.config.data.FoxcordData()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(
        description="Get system information foxcord is running on.",
        aliases=['si']
    )
    @commands.has_any_role(
        bot_data.dev_id
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def sysinfo(self, ctx):
        await ctx.send(f"OS: {platform.system()}\n"
                       f"OS Version: {platform.version()}\n"
                       f"{'OS Edition: ' + platform.win32_edition() if platform.system() == 'Windows' else ''}\n")

def setup(bot):
    bot.add_cog(SysInfo(bot))
