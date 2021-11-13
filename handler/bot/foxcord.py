import disnake
from handler.logging.log import Log
from handler.config.data import Data
from handler.database.sql import Sql
from handler.commands.controller import FoxcordCommands
from disnake.ext import commands


class Foxcord(commands.Bot):

    f_data = Data().read()
    f_bot_log = Log().create(__name__, f_data.bot_log)
    f_sql = Sql()
    foxcord = commands.Bot(command_prefix=f_data.prefix, test_guilds=[880443032246317076])
    f_commands = FoxcordCommands(foxcord)

    def init(self):
        if self.f_data.token is None or self.f_data.prefix is None:
            self.f_bot_log.error(f"Cannot find token or a set prefix.")
            exit(1)
        self.f_commands.load()

    async def on_ready(self):
        self.f_bot_log.info("Foxcord is connected")
        self.f_bot_log.info(f"Commands loaded -> {self.f_commands.total_loaded}")

    async def on_message(self, message: disnake.Message):
        if message.author == self.user:
            return

    async def on_slash_command(self, ctx: commands.Context):
        self.f_bot_log.info(f"Slash command: {ctx.command} invoked by {ctx.author}")

    async def on_slash_command_completion(self, ctx: commands.Context):
        self.f_bot_log.info(f"Slash command: {ctx.command} invoked by {ctx.author} successful")

    async def on_slash_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingAnyRole):
            if self.f_data.command_warnings:
                self.f_bot_log.warning(f"{ctx.author} is missing roles for slash command {ctx.message}")
            if self.f_data.command_debug or self.f_data.mode == "development":
                self.f_bot_log.debug(f"Command -> {ctx.command} | Invoked from -> {ctx.command.__name__} | By user"
                                     f"-> {ctx.author} | Error -> {ctx.author} missing roles")
            await ctx.send(f"{ctx.author.mention}, you don't have the required permissions for this command.")
