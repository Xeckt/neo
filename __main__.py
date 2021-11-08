import sys
import handler.config.data
import handler.logging.foxlog
import handler.commands.controller
import handler.database.sql
from discord.ext import commands

foxcord_data = handler.config.data.FoxcordData()
foxcord_data.read_bot_config()

command_log = handler.logging.foxlog.Log().create_logger("COMMANDS", foxcord_data.command_log)
foxlog = handler.logging.foxlog.Log().create_logger(__name__, foxcord_data.log)

foxcord = commands.Bot(command_prefix=foxcord_data.prefix)
foxcord_commands = handler.commands.controller.FoxcordCommands(foxcord)

foxcord_db = handler.database.sql.Sql()

@foxcord.event
async def on_ready():
    foxlog.info(f"Foxcord is connected")
    command_log.info(f"Commands loaded: {foxcord_commands.total_loaded}")


async def on_message(ctx):
    pass


@foxcord.event
async def on_command(ctx):
    if foxcord_data.command_debug:
        command_log.debug(f"Command invoked by {ctx.author}: {ctx.message.content}")


@foxcord.event
async def on_command_completion(ctx):
    if foxcord_data.command_debug:
        command_log.debug(f"Command: {ctx.command} invocation successful by: {ctx.author}")


@foxcord.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        if foxcord_data.command_warnings or foxcord_data.command_debug:
            command_log.warning(f"Invalid user role for user: {ctx.author} with command: {ctx.command}")
        await ctx.send(f"{ctx.author.mention}, you don't have the required permissions for this command!")


def init():
    check()
    foxcord_commands.load()
    if foxcord_data.database_enabled:
        foxcord_db.create_pool()
    foxcord.run(foxcord_data.token)


def check():
    if not str(foxcord_data.prefix):
        foxlog.error("Cannot find prefix in Foxcord configuration")
        exit(1)
    if not str(foxcord_data.token):
        foxlog.error("Cannot find token in Foxcord configuration")
        exit(1)


if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 10):
        foxlog.error(
            f"Python version must be minimum 3.10. Currently detected version: "
            f"{str(sys.version_info.major) + '.' + str(sys.version_info.minor)}")
        exit(1)
    init()
