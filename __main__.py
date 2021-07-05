import discord
import handler.config.data
import handler.logging.bot_log
import settings.constants


class Foxcord(discord.Client):

    bot_data = handler.config.data.BotData()
    constants = settings.constants
    log = handler.logging.bot_log.BotLog().setup_log(__name__, constants.BOT_LOG_PATH)

    async def on_ready(self):
        self.log.info(f"[BOT] -> {self.user} connected to guild {discord.utils.get(self.guilds)}")

    async def on_message(self, ctx):
        pass

    def prepare_bot(self):
        self.bot_data.read_bot_config()

    def init(self):
        self.prepare_bot()
        self.run(self.bot_data.get_token())


if __name__ == "__main__":
    Foxcord().init()
