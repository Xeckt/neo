import yaml
import dotenv


class Data:
    env_keys = ['TOKEN', 'SQL_HOST', 'SQL_PORT',
                'SQL_USER', 'SQL_PASS', 'SQL_DB']
    yaml_file = 'settings/yadps.yaml'

    config = {
        'version': '',
        'token': '',
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
        with open(self.yaml_file) as stream:
            y_dict = yaml.safe_load(stream)
            y_arr = []
            for j in y_dict:
                y_arr.append(j)
                for j in range(0, len(y_arr)):
                    for k in y_dict[y_arr[j]]:
                        Data.config[k] = y_dict[y_arr[j]][k]

    def read_env(self):
        env = dotenv.dotenv_values(self.config['envFile'])
        for v in self.env_keys:
            Data.config[v.lower()] = env.get(v.upper())

    def read(self):
        Data().read_env()
        Data().read_yaml()
        return Data()
