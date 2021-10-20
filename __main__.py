import handler.config.data
import handler.logging.foxlog
import handler.commands.controller
import settings.constants
import discord
from discord.ext import commands

constants = settings.constants

bot_data = handler.config.data.BotData()
bot_data.read_bot_config()

command_log = handler.logging.foxlog.BotLog().setup_log("COMMANDS", constants.COMMANDS_LOG_PATH)
foxlog = handler.logging.foxlog.BotLog().setup_log(__name__, constants.BOT_LOG_PATH)

foxcord = commands.Bot(command_prefix=bot_data.get_prefix())


async def on_ready(ctx):
    foxlog.info(f"[BOT] -> {ctx.user} connected to guild {discord.utils.get(ctx.guilds)}")


async def on_message(ctx):
    pass


@foxcord.event
async def on_command(ctx):
    if constants.ENABLE_COMMAND_DEBUG:
        command_log.debug(f"Command invoked by {ctx.author}: {ctx.message.content}")


@foxcord.event
async def on_command_completion(ctx):
    if constants.ENABLE_COMMAND_DEBUG:
        command_log.debug(f"Command: {ctx.command} invocation successful by: {ctx.author}")


@foxcord.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        if constants.ENABLE_COMMAND_WARNINGS or constants.ENABLE_COMMAND_DEBUG:
            command_log.warning(f"Invalid user role for user: {ctx.author} with command: {ctx.command}")
        await ctx.send(f"{ctx.author.mention}, you don't have the required permissions for this command!")

def init():
    check()
    commands = handler.commands.controller.FoxcordCommands(foxcord)
    commands.load()
    foxcord.run(bot_data.get_token())


def check():
    if not str(bot_data.get_prefix()):
        foxlog.error("Cannot find prefix in Foxcord configuration")
        exit(1)
    if not str(bot_data.get_token()):
        foxlog.error("Cannot find token in Foxcord configuration")
        exit(1)


if __name__ == "__main__":
    init()
