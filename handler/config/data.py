import json
import handler.logging.foxlog
import settings.constants as constants


class BotData:
    foxlog = handler.logging.foxlog.BotLog().setup_log(__name__, constants.BOT_LOG_PATH)
    bot_token = ''
    bot_prefix = ''

    def __init__(self):
        self.bot_config_path = constants.BOT_CONFIG_PATH

    def read_bot_config(self):
        self.foxlog.info("Reading Foxcord config")
        with open(self.bot_config_path, "r") as bot_config:
            data = json.load(bot_config)
            for bot_data in data["bot"]:
                self.set_prefix(bot_data["prefix"])
                self.set_token(bot_data["token"])
        bot_config.close()

    def get_prefix(self):
        return BotData.bot_prefix

    def get_token(self):
        return BotData.bot_token

    def set_prefix(self, prefix):
        BotData.bot_prefix = prefix
        return BotData.bot_prefix

    def set_token(self, token):
        BotData.bot_token = token
        return BotData.bot_token
