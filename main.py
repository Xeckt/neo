import sys
from neo.config.data import Data
from neo.bot.neo import Neo


if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 10):
        print(f"Python version must be minimum 3.10. Currently detected version: "
              f"{str(sys.version_info.major) + '.' + str(sys.version_info.minor)}")
        exit(1)
    data = Data()
    neo = Neo(test_guilds=[data.guildId])
    neo.run(neo.data.token)

