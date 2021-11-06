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
    async def commandtool(self, ctx, command_rank, state, command):
        self.commands.set_command_state(command_rank, state, command)
        await ctx.send(f"Command state: `{state}` on `{command}` successful")


def setup(bot):
    bot.add_cog(CommandTool(bot))
