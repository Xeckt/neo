import yaml
import dotenv


class FoxcordData:
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
    log = ''
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

    def read_settings(self):
        env_data = dotenv.dotenv_values('settings/.env')
        FoxcordData.token = env_data.get('TOKEN')
        FoxcordData.sql_host = env_data.get('SQL_HOST')
        FoxcordData.sql_port = env_data.get('SQL_PORT')
        FoxcordData.sql_user = env_data.get('SQL_USER')
        FoxcordData.sql_pass = env_data.get('SQL_PASS')
        FoxcordData.sql_db = env_data.get('SQL_DB')

        with open("settings/foxcord.yaml", "r") as settings:
            yaml_data = yaml.load(settings, Loader=yaml.loader.Loader)
            for (foxcord_data, log_data, cmd_data, role_data) in zip(
                    yaml_data["foxcord"],
                    yaml_data["logData"],
                    yaml_data["commandData"],
                    yaml_data["roleData"],
            ):
                FoxcordData.version = foxcord_data['version']
                FoxcordData.prefix = foxcord_data['prefix']
                FoxcordData.sql_enabled = foxcord_data['databaseEnabled']
                FoxcordData.mode = foxcord_data['mode']

                FoxcordData.user_commands = cmd_data['enableUserCommands']
                FoxcordData.mod_commands = cmd_data['enableModCommands']
                FoxcordData.admin_commands = cmd_data['enableAdminCommands']
                FoxcordData.dev_commands = cmd_data['enableDevCommands']
                FoxcordData.command_warnings = cmd_data['enableCommandWarnings']
                FoxcordData.command_debug = cmd_data['enableCommandDebug']

                FoxcordData.enable_logging = log_data['enableLogging']
                FoxcordData.log = log_data['botLog']
                FoxcordData.database_log = log_data['databaseLog']
                FoxcordData.command_log = log_data['commandLog']

                FoxcordData.cog_path = cmd_data['cogPath']
                FoxcordData.user_cog = cmd_data['userCog']
                FoxcordData.mod_cog = cmd_data['modCog']
                FoxcordData.admin_cog = cmd_data['adminCog']
                FoxcordData.dev_cog = cmd_data['devCog']

                FoxcordData.user_id = role_data['memberRoleId']
                FoxcordData.mod_id = role_data['modRoleId']
                FoxcordData.admin_id = role_data['adminRoleId']
                FoxcordData.dev_id = role_data['devRoleId']
        settings.close()
