import disnake
from handler.logging.log import Log
from handler.config.data import Data
from handler.database.sql import Sql
from handler.commands.controller import CommandController
from disnake.ext import commands


class Foxcord(commands.Bot):
    f_data = Data().read()
    f_bot_log = Log().create(__name__, f_data.bot_log)
    f_sql = Sql()
    f_cmd_controller = CommandController

    def init(self):
        self.f_bot_log.info("Initing Foxcord")
        self.f_cmd_controller(self).init()
        self.f_sql.init()
        if self.f_data.token == "":
            self.f_bot_log.error("Token not found!")
            exit(1)
        if self.f_data.prefix == "":
            self.f_bot_log.warn("Prefix not found!")
        self.f_bot_log.info("Valid .env configuration detected")

    async def on_ready(self):
        self.f_bot_log.info("Foxcord is connected")

    async def on_message(self, message: disnake.Message):
        if message.author == self.user:
            return

    async def on_slash_command(self, inter):
        self.f_bot_log.info(f"Slash command: {inter.data.name} invoked by {inter.author}")

    async def on_slash_command_completion(self, inter):
        self.f_bot_log.info(f"Slash command: {inter.data.name} invoked by {inter.author} successful")

    async def on_slash_command_error(self, inter, error):
        self.f_bot_log.error(inter, error)
        if isinstance(error, commands.MissingAnyRole):
            if self.f_data.command_warnings:
                self.f_bot_log.warning(f"{inter.author} is missing roles for slash command: {inter.data.name}")
            if self.f_data.command_debug or self.f_data.mode == "development":
                self.f_bot_log.debug(f"Command -> {inter.data.name} | Invoked from -> {inter.channel_id} | By user"
                                     f"-> {inter.author} | Error -> {inter.author} missing roles")
            await inter.send(f"{inter.author.mention}, you don't have the required permissions for this command.")
