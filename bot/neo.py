#!/usr/bin/env python
import disnake
from typing import Any
from config.neoconfig import NeoConfig
from logger.log import Log
from database.sql import Sql
from commands.controller import CommandController
from disnake.ext import commands

class Neo(commands.Bot):
    data = NeoConfig()
    command_controller = CommandController
    log = Log().create(__name__, data.botLog)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.log.info("Neo is starting")
        self.command_controller(self).load_cmds()
        if self.data.databaseEnabled:
            self.log.info("Database is enabled, starting")
            sql = Sql()
            if not sql.start():
                self.log.warn("SQL couldn't start or didn't update status to loaded, exiting.")
                exit(1)
            self.log.info("SQL has started!")
        else:
            self.log.warn("SQL is disabled, skipping")

    async def on_ready(self):
        self.log.info("Neo is connected")

    async def on_message(self, interaction: disnake.InteractionMessage):
        if interaction.author == self.user:
            return

    async def on_slash_command(self, inter: disnake.ApplicationCommandInteraction):
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author}")

    async def on_slash_command_completion(self, inter: disnake.ApplicationCommandInteraction):
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author} successful")

    async def on_slash_command_error(self, interaction: disnake.ApplicationCommandInteraction, error):
        match error:
            case commands.MissingAnyRole:
                self.log.warning(f"{interaction.author} is missing roles for command: {interaction.data.name}")
            case commands.MissingRequiredArgument:
                await interaction.send(f"You are missing a required argument in your command.")
            case commands.ArgumentParsingError:
                await interaction.send("I seem to have an issue parsing the arguments you have given me for your command.")
            case _:
                await interaction.send("There was an error trying to use this command. Contact an Administrator to check "
                                   "the logs.")
                self.log.error(error)

