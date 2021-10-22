from discord.ext import commands
import handler.commands.controller
import handler.config.data


class CommandTool(commands.Cog):

    bot_data = handler.config.data.FoxcordData()

    def __init__(self, bot):
        self.bot = bot
        self.commands = handler.commands.controller.FoxcordCommands(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command(
        description="Load a command module",
        aliases=['cmdtool', 'ctool'],
        hidden=True
    )
    @commands.has_any_role(
        bot_data.admin_id,
        bot_data.dev_id
    )
    async def commandtool(self, ctx, command_rank, command, parameter):
        self.commands.set_command(command_rank, parameter, command)
        await ctx.send(f"Command operation: `{parameter}` on `{command}` successful")


def setup(bot):
    bot.add_cog(CommandTool(bot))
