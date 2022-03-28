import sys
from handler.bot.yadps import Yadps
from handler.commands.controller import CommandController
from handler.config.newdata import NewData
import disnake

if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 10):
        print(
            f"Python version must be minimum 3.10. Currently detected version: "
            f"{str(sys.version_info.major) + '.' + str(sys.version_info.minor)}")
        exit(1)
    bot = Yadps(command_prefix=Yadps.data.prefix)
    bot.init()
    bot.run(bot.data.token)

