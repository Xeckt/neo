import sys
import unittest
import dotenv
import yaml
from schema import Schema, SchemaError



class TestActions(unittest.TestCase):
    def test_assertPythonVersion(self):
        self.assertTrue(sys.version_info[0:2] == (3, 10))

    def test_assertTokenExists(self):
        def token_exists() -> bool:
            env = dotenv.dotenv_values("settings/.env")
            if "TOKEN" not in env:
                print("[ERROR] -> Missing key: TOKEN")
                return False
            for k, v in env.items():
                if k == "TOKEN" and len(v) == 0:
                    print("[ERROR] -> Invalid TOKEN value")
                    return False
            return True
        self.assertTrue(token_exists())

    def test_assertValidConfig(self):
        def valid_yaml() -> bool:
            yadps_schema = Schema({
                "yadps": {
                    "version": str,
                    "databaseEnabled": bool,
                    "mode": str,
                    "envFile": str,
                },
                "logData": {
                    "enableLogging": bool,
                    "botLog": str,
                    "databaseLog": str,
                    "commandLog": str,
                    "systemLog": str,
                },
                "commandData": {
                    "cogPath": str,
                    "userCog": str,
                    "modCog": str,
                    "adminCog": str,
                    "devCog": str,
                    "enableUserCommands": bool,
                    "enableModCommands": bool,
                    "enableAdminCommands": bool,
                    "enableDevCommands": bool,
                    "enableCommandWarnings": bool,
                    "enableCommandDebug": bool,
                },
                "roleData": {
                    "guildId": int,
                    "memberRoleId": int,
                    "modRoleId": int,
                    "adminRoleId": int,
                    "devRoleId": int,
                }
            })
            with open("settings/yadps.yaml", 'r') as stream:
                y = yaml.safe_load(stream)
            try:
                yadps_schema.validate(y)
                return True
            except SchemaError as err:
                print(err)
                return False
        self.assertTrue(valid_yaml())
