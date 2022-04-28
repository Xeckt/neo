import sys
import disnake
from foxcord.bot.foxcord import Yadps
from foxcord.config.data import Data

if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 10):
        print(f"Python version must be minimum 3.10. Currently detected version: "
              f"{str(sys.version_info.major) + '.' + str(sys.version_info.minor)}")
        exit(1)
    foxcord = Foxcord(test_guilds=[956780366063095808], intents=disnake.Intents.default())
    foxcord.run(foxcord.data.token)
