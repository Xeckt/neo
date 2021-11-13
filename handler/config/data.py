import yaml
import dotenv


class Data:
    version = ''
    token = ''
    prefix = ''
    mode = None

    sql_enabled = False
    sql_host = ''
    sql_port = ''
    sql_user = ''
    sql_pass = ''
    sql_db = ''

    user_commands = False
    mod_commands = False
    admin_commands = False
    dev_commands = False
    command_warnings = False
    command_debug = False

    enable_logging = False
    bot_log = ''
    database_log = ''
    command_log = ''

    cog_path = ''
    user_cog = ''
    mod_cog = ''
    admin_cog = ''
    dev_cog = ''

    user_id = 0
    mod_id = 0
    admin_id = 0
    dev_id = 0

    def read(self):
        env_data = dotenv.dotenv_values('settings/.env')
        Data.token = env_data.get('TOKEN')
        Data.sql_host = env_data.get('SQL_HOST')
        Data.sql_port = env_data.get('SQL_PORT')
        Data.sql_user = env_data.get('SQL_USER')
        Data.sql_pass = env_data.get('SQL_PASS')
        Data.sql_db = env_data.get('SQL_DB')

        with open("settings/foxcord.yaml", "r") as settings:
            yaml_data = yaml.load(settings, Loader=yaml.loader.Loader)
            for (foxcord_data, log_data, cmd_data, role_data) in zip(
                    yaml_data["foxcord"],
                    yaml_data["logData"],
                    yaml_data["commandData"],
                    yaml_data["roleData"],
            ):
                Data.version = foxcord_data['version']
                Data.prefix = foxcord_data['prefix']
                Data.sql_enabled = foxcord_data['databaseEnabled']
                Data.mode = foxcord_data['mode']

                Data.user_commands = cmd_data['enableUserCommands']
                Data.mod_commands = cmd_data['enableModCommands']
                Data.admin_commands = cmd_data['enableAdminCommands']
                Data.dev_commands = cmd_data['enableDevCommands']
                Data.command_warnings = cmd_data['enableCommandWarnings']
                Data.command_debug = cmd_data['enableCommandDebug']

                Data.enable_logging = log_data['enableLogging']
                Data.bot_log = log_data['botLog']
                Data.database_log = log_data['databaseLog']
                Data.command_log = log_data['commandLog']

                Data.cog_path = cmd_data['cogPath']
                Data.user_cog = cmd_data['userCog']
                Data.mod_cog = cmd_data['modCog']
                Data.admin_cog = cmd_data['adminCog']
                Data.dev_cog = cmd_data['devCog']

                Data.user_id = role_data['memberRoleId']
                Data.mod_id = role_data['modRoleId']
                Data.admin_id = role_data['adminRoleId']
                Data.dev_id = role_data['devRoleId']
        settings.close()
        return Data
