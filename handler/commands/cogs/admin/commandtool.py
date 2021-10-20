from discord.ext import commands
import settings.constants as constants
import handler.commands.controller
import string


class CommandTool(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.commands = handler.commands.controller.FoxcordCommands(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.has_any_role(constants.ADMIN_ROLE_ID)
    @commands.command(
        description="Load a command module",
        hidden=True
    )
    @commands.has_any_role(constants.ADMIN_ROLE_ID)
    async def cmdtool(self, ctx, command_rank, command, parameter):
        if parameter.lower() == "load":
            self.commands.load_command(command_rank, command)
        if parameter.lower() == "reload":
            self.commands.reload_command(command_rank, command)
        if parameter.lower() == "unload":
            self.commands.unload_command(command_rank, command)
        ctx.send(f"Command: {command} reloaded for: {command_rank}")

def setup(bot):
    bot.add_cog(CommandTool(bot))
