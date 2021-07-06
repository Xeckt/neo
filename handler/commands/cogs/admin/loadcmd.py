from discord.ext import commands
import settings.constants as constants

class Load(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(
        description="Load a command module",
        hidden=True
    )
    @commands.has_any_role(constants.ADMIN_ROLE_ID)
    async def load(self, message, command_rank, command):
        self.bot.load_extension(f'cogs.commands.{command_rank}.{command}')
        await message.send(f"Loaded command: {command}")


def setup(bot):
    bot.add_cog(Load(bot))
