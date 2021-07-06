from discord.ext import commands
import settings.constants as constants


class Reload(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(
        description="Reload a command module",
        hidden=True
    )
    @commands.has_any_role(constants.ADMIN_ROLE_ID)
    async def reload(self, message, command_rank, command):
        self.bot.reload_extension(f'cogs.commands.{command_rank}.{command}')
        await message.send(f"Reloaded command: {command}")


def setup(bot):
    bot.add_cog(Reload(bot))
