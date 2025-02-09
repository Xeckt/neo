#!/usr/bin/env python
import sys

import disnake
from typing import Any
from settings import NeoConfig
from log import Log
from sql import Sql
from commands.controller import CommandController
from disnake.ext import commands

class Neo(commands.InteractionBot):
    data = NeoConfig()
    command_controller = CommandController
    log = Log().create(__name__, data.botLog)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

    def run_bot(self):
        if self.data.token is None or len(self.data.token) == 0:
            self.log.error("Token not found or is empty, exiting")
            exit(1)

        self.log.info("Neo is starting")
        self.command_controller(self, self.data).load_cmds()

        if self.data.databaseEnabled:
            self.log.info("Database is enabled, starting")
            sql = Sql(self.data)
            if not sql.start():
                self.log.warn("SQL couldn't start or didn't update status to loaded, exiting.")
                exit(1)
            self.log.info("SQL has started!")
        else:
            self.log.warn("SQL is disabled, skipping")
        self.run(self.data.token)

    async def on_ready(self):
        self.log.info("Neo is connected")

    async def on_message(self, interaction: disnake.InteractionMessage):
        if interaction.author == self.user:
            return

    async def on_slash_command(self, inter: disnake.ApplicationCommandInteraction):
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author}")

    async def on_slash_command_completion(self, inter: disnake.ApplicationCommandInteraction):
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author} successful")

    async def on_slash_command_error(self, interaction: disnake.ApplicationCommandInteraction, exception):
        match exception:
            case commands.MissingAnyRole:
                self.log.warning(f"{interaction.author} is missing roles for command: {interaction.data.name}")
            case commands.MissingRequiredArgument:
                await interaction.send(f"You are missing a required argument in your command.")
            case commands.ArgumentParsingError:
                await interaction.send("I seem to have an issue parsing the arguments you have given me for your command.")
                self.log.error(exception)
            case _:
                await interaction.send(f"There was an error trying to use this command. See console log for more details.")
                self.log.error(exception)

Neo().run_bot()
