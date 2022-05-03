#!/usr/bin/env python

from typing import Any
import disnake
from neo.logging.log import Log
from neo.config.data import Data
from neo.database.sql import Sql
from neo.commands.controller import CommandController
from test.test_actions import TestActions
from disnake.ext import commands


class Neo(commands.Bot):
    test = TestActions()
    test.assertTokenValidity()
    test.assertValidConfig()
    data = Data()
    log = Log().create(__name__, data.botLog)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.log.info("Neo is starting -> loading command controller")
        self.command_controller = CommandController(self).load()
        if self.data.databaseEnabled:
            self.log.info("Database is enabled, starting")
            self.sql = Sql()
            if self.sql.loaded:
                self.log.info("Database successfully started")
        else:
            self.log.warn("SQL IS DISABLED")

    async def on_ready(self):
        self.log.info("neo is now connected, enjoy your stay.")

    async def on_message(self, interaction: disnake.InteractionMessage):
        if interaction.author == self.user:
            return

    async def on_slash_command(self, inter: disnake.ApplicationCommandInteraction):
        if self.data.enableCommandDebug:
            self.log.debug(f"Slash command {inter.data.name} invoked by {inter.author} result -> {inter.data}")
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author}")

    async def on_slash_command_completion(self, inter: disnake.ApplicationCommandInteraction):
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author} successful")

    async def on_slash_command_error(self, interaction: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.MissingAnyRole):
            if self.data.enableCommandWarnings:
                self.log.warning(f"{interaction.author} is missing roles for command: {interaction.data.name}")
            if self.data.enableCommandDebug or self.data.mode == "development":
                self.log.debug(
                    f"Command -> {interaction.data.name} | Invoked from -> {interaction.channel_id} | By user"
                    f"-> {interaction.author} | Error -> {interaction.author} missing roles")
            await interaction.send(
                f"{interaction.author.mention}, you don't have the required permissions for this command.")
        self.log.error(error)

