#!/usr/bin/env python

from typing import Any
import disnake
from yadps.logging.log import Log
from yadps.config.data import Data
from yadps.database.sql import Sql
from yadps.commands.controller import CommandController
from test.test_actions import TestActions
from disnake.ext import commands


class Yadps(commands.Bot):
    data = Data()
    test = TestActions()
    log = Log().create(__name__, data.config["botLog"])

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.log.info("YADPS-Chan is starting")
        self.test.assertTokenValidity()
        self.test.assertValidConfig()
        self.command_controller = CommandController(self).load()
        if self.data.config["sql_enabled"]:
            self.sql = Sql()
        else:
            self.log.warn("SQL IS DISABLED")

    async def on_ready(self):
        self.log.info("yadps-chan is connected")

    async def on_message(self, interaction: disnake.ApplicationCommandInteraction):
        if interaction.author == self.user:
            return

    async def on_slash_command(self, inter):
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author}")

    async def on_slash_command_completion(self, inter):
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author} successful")

    async def on_slash_command_error(self, interaction: disnake.ApplicationCommandInteraction, error):
        print(error)
        if isinstance(error, commands.MissingAnyRole):
            if self.data.config["enableCommandWarnings"]:
                self.log.warning(f"{interaction.author} is missing roles for command: {interaction.data.name}")
            if self.data.config["enableCommandDebug"] or self.data.config["mode"] == "development":
                self.log.debug(
                    f"Command -> {interaction.data.name} | Invoked from -> {interaction.channel_id} | By user"
                    f"-> {interaction.author} | Error -> {interaction.author} missing roles")
            await interaction.send(
                f"{interaction.author.mention}, you don't have the required permissions for this command.")

