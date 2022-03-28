import disnake
from disnake.ext import commands
from handler.commands.controller import CommandController
from handler.config.data import Data


# This command is in progress so may look unfinished.

class CommandTool(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot
        self.commands = CommandController(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Interact with the built in command controller module",
        aliases=['cmdtool', 'ctool'],
    )
    @commands.has_any_role(
        data.admin_id,
        data.dev_id
    )
    async def commandtool(self, interaction: disnake.ApplicationCommandInteraction, command_rank, command,
                          state: str):
        self.commands.set_command_state(command_rank, state, command)
        await interaction.send(f"Command: `{command}` is now in the `{state}` state")

    @commandtool.autocomplete("state")
    async def state_options(self, inter: disnake.ApplicationCommandInteraction, user_input: str):
        options = ["load", "unload", "reload"]
        return [option for option in options if user_input.lower() in option]

    @commandtool.autocomplete("command_rank")
    async def rank_options(self, inter: disnake.ApplicationCommandInteraction, user_input: str):
        options = self.commands.get_command_ranks()
        return [option for option in options if user_input.lower() in option]

    @commandtool.autocomplete("command")
    async def command_options(self, inter: disnake.ApplicationCommandInteraction, user_input: str):
        options = self.commands.get_command_list()
        return [option for option in options if user_input.lower() in option]


def setup(bot):
    bot.add_cog(CommandTool(bot))
