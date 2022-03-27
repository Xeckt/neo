import sys
from handler.bot.yadps import Yadps
from handler.commands.controller import CommandController
import disnake

if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 10):
        print(
            f"Python version must be minimum 3.10. Currently detected version: "
            f"{str(sys.version_info.major) + '.' + str(sys.version_info.minor)}")
        exit(1)
    bot = Yadps(command_prefix=Yadps.f_data.prefix, test_guilds=[909578544869437460])
    bot.init()
    bot.run(bot.f_data.token)

