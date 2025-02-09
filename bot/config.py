import os

import yaml
import dotenv


class NeoConfig:
    env_keys = ['TOKEN', 'SQL_HOST', 'SQL_PORT', 'SQL_USER', 'SQL_PASS', 'SQL_DB']
    yaml_file = './conf/neo.yaml'

    def __init__(self):
        # Neo config vars read() will attach to
        # This isn't actually necessary but makes it resolvable in the source
        # So if you don't care about unresolved syntax errors you can remove all the definitions

        # bot:
        self.version = 0
        self.databaseEnabled = False
        # bot

        # logData
        self.enableLogging = False
        self.botLog = ""
        self.databaseLog = ""
        self.commandLog = ""
        self.systemLog = ""
        # logData

        # roleData
        self.guildId = 0
        self.memberRoleId = 0
        self.modRoleId = 0
        self.adminRoleId = 0
        self.devRoleId = 0
        # roleData

        # database
        self.sql_host = ""
        self.sql_port = 0
        self.sql_user = ""
        self.sql_pass = ""
        self.sql_db = ""
        # database

        # token
        self.token = "" # TODO: This var should get cleared once loaded into the Discord connection
        # token
        print(os.getcwd())
        with open(self.yaml_file) as stream:
            y_dict = yaml.safe_load(stream)
            for block in y_dict.values():
                for key, value in block.items():
                    setattr(self, key, value)
            env = dotenv.dotenv_values("./conf/.env")
            for v in self.env_keys:
                setattr(self, v.lower(), env.get(v.upper()))

