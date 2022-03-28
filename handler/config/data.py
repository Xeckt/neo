import yaml
import dotenv



class Data:
    env_keys = ['TOKEN', 'SQL_HOST', 'SQL_PORT', 'SQL_USER', 'SQL_PASS', 'SQL_DB']
    yaml_file = 'settings/yadps.yaml'

    config = {
        'version': '',
        'token': '',
        'prefix': '',
        'mode': None,
        'envFile': 'settings/.env',
        'sql_enabled': False,
        'sql_host': '',
        'sql_port': '',
        'sql_user': '',
        'sql_pass': '',
        'sql_db': '',
        'enableLogging': False,
        'botLog': '',
        'databaseLog': '',
        'commandLog': '',
        'cogPath': '',
        'userCog': '',
        'modCog': '',
        'adminCog': '',
        'devCog': '',
        'enableUserCommands': False,
        'enableModCommands': False,
        'enableAdminCommands': False,
        'enableDevCommands': False,
        'enableCommandWarnings': False,
        'enableCommandDebug': False,
        'guildId': 0,
        'memberRoleId': 0,
        'modRoleId': 0,
        'adminRoleId': 0,
        'devRoleId': 0,
    }

    def read_yaml(self):
        with open(self.yaml_file) as settings:
            data = yaml.load(settings, Loader=yaml.loader.Loader)
            dicts_arr = []
            for (bot, log, cmd, role) in zip(
                    data["yadps"],
                    data["logData"],
                    data["commandData"],
                    data["roleData"],
            ):
                dicts_arr.append(bot)
                dicts_arr.append(log)
                dicts_arr.append(cmd)
                dicts_arr.append(role)
            for i in range(0, len(dicts_arr)):
                for k, v in dicts_arr[i].items():
                    Data().config[k] = v

    def read_env(self):
        env = dotenv.dotenv_values(self.config['envFile'])
        for v in self.env_keys:
            Data.config[v.lower()] = env.get(v.upper())

    def read(self):
        Data().read_env()
        Data().read_yaml()
        return Data()
