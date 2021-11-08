import json


class FoxcordData:
    version = ''
    token = ''
    prefix = ''

    enable_bot_log = False
    user_commands = False
    mod_commands = False
    admin_commands = False
    dev_commands = False
    command_warnings = False
    command_debug = False

    log = ''
    command_log = ''
    system_log = ''

    cog_path = ''
    user_cog = ''
    mod_cog = ''
    admin_cog = ''
    dev_cog = ''

    user_id = 0
    mod_id = 0
    admin_id = 0
    dev_id = 0

    def read_bot_config(self):
        with open("settings/foxcord.json", "r") as bot_config:
            data = json.load(bot_config)
            for (bot_data, log_data, cmd_data, role_data) in zip(
                    data["bot"],
                    data["logData"],
                    data["commandData"],
                    data["roleData"],
            ):
                FoxcordData.version = bot_data['version']
                FoxcordData.token = bot_data['token']
                FoxcordData.prefix = bot_data['prefix']

                FoxcordData.enable_bot_log = bot_data['enableBotLog']
                FoxcordData.user_commands = cmd_data['enableUserCommands']
                FoxcordData.mod_commands = cmd_data['enableModCommands']
                FoxcordData.admin_commands = cmd_data['enableAdminCommands']
                FoxcordData.dev_commands = cmd_data['enableDevCommands']
                FoxcordData.command_warnings = cmd_data['enableCommandWarnings']
                FoxcordData.command_debug = cmd_data['enableCommandDebug']

                FoxcordData.log = log_data['botLog']
                FoxcordData.command_log = log_data['commandLog']
                FoxcordData.system_log = log_data['systemLog']

                FoxcordData.cog_path = cmd_data['cogPath']
                FoxcordData.user_cog = cmd_data['userCog']
                FoxcordData.mod_cog = cmd_data['modCog']
                FoxcordData.admin_cog = cmd_data['adminCog']
                FoxcordData.dev_cog = cmd_data['devCog']

                FoxcordData.user_id = role_data['userId']
                FoxcordData.mod_id = role_data['modId']
                FoxcordData.admin_id = role_data['adminId']
                FoxcordData.dev_id = role_data['devId']
        bot_config.close()
