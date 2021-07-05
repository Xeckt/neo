import json
import settings.constants as constants


class BotData:
    bot_token = ''
    bot_prefix = ''

    def __init__(self):
        self.bot_config_path = constants.BOT_CONFIG_PATH

    def read_bot_config(self):
        with open(self.bot_config_path, "r") as bot_config:
            data = json.load(bot_config)
            for bot_data in data["bot"]:
                if bot_data["token"] == "" or bot_data["prefix"] == "":
                    # TODO LOG RETURN EMPTY VALUES
                    return
                self.set_bot_prefix(bot_data["prefix"])
                self.set_bot_token(bot_data["token"])
        bot_config.close()

    def get_bot_prefix(self):
        return BotData.bot_prefix

    def set_bot_prefix(self, prefix):
        BotData.bot_prefix = prefix
        return BotData.bot_prefix

    def set_bot_token(self, token):
        BotData.bot_token = token
        return BotData.bot_token

    def get_bot_token(self):
        return BotData.bot_token
