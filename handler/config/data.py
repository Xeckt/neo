import json
import settings.constants as constants


class BotData:
    def __init__(self):
        self.bot_config_path = constants.BOT_CONFIG_PATH
        self.bot_token = ''
        self.bot_prefix = ''

    def read_bot_config(self):
        with open(self.bot_config_path, "r") as bot_config:
            data = json.load(bot_config)
            for bot_data in data["bot"]:
                if bot_data["token"] == "" or bot_data["prefix"] == "":
                    # TODO LOG RETURN EMPTY VALUES
                    return
                self.bot_token = bot_data["token"]
                self.bot_prefix = bot_data["prefix"]
        bot_config.close()

    def get_bot_prefix(self):
        return self.bot_prefix

    def set_bot_prefix(self, prefix):
        self.bot_prefix = prefix
        return self.bot_prefix

    def set_bot_token(self, token):
        self.bot_token = token
        return self.bot_token

    def get_bot_token(self):
        return self.bot_token


BotData().read_bot_config()
