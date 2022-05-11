import sys
from neo.bot.neo import Neo

if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 10):
        print(f"Python version must be minimum 3.10. Currently detected version: "
              f"{str(sys.version_info.major) + '.' + str(sys.version_info.minor)}")
        exit(1)
    neo = Neo(test_guilds=[])
    neo.run(neo.data.token)

