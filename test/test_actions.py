import sys
import unittest
import dotenv
import yaml
from schema import Schema, SchemaError
from logger.log import Log
from config.neoconfig import NeoConfig


class TestActions(unittest.TestCase):
    data = NeoConfig()
    log = Log().create(__name__, "logs/test.logs")

    def assertValidConfig(self):
        neo_schema = Schema({
            "neo": {
                "version": str,
                "databaseEnabled": bool,
                "mode": str,
            },
            "logData": {
                "enableLogging": bool,
                "botLog": str,
                "databaseLog": str,
                "commandLog": str,
                "systemLog": str,
            },
            "roleData": {
                "guildId": int,
                "memberRoleId": int,
                "modRoleId": int,
                "adminRoleId": int,
                "devRoleId": int,
            }
        })
        
        with open("settings/neo.yaml", 'r') as stream:
            y = yaml.safe_load(stream)
        try:
            neo_schema.validate(y)
        except SchemaError as err:
            self.log.error(err)
            self.fail()
