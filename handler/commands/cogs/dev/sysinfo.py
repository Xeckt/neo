from disnake.ext import commands
from handler.config.data import Data
import platform


class SysInfo(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Get system information Foxcord is running on.",
        aliases=['si']
    )
    @commands.has_any_role(
        data.dev_id
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def sysinfo(self, ctx):
        await ctx.send(f"OS: {platform.system()}\n"
                       f"OS Version: {platform.version()}\n"
                       f"{'OS Edition: ' + platform.win32_edition() if platform.system() == 'Windows' else ''}\n")


def setup(bot):
    bot.add_cog(SysInfo(bot))
