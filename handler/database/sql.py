import asyncpg, asyncio
import handler.config.data
import handler.logging.log


class Sql:

    def __init__(self):
        self.f_data = handler.config.data.Data()
        self.f_log = handler.logging.log.Log().create(__name__, self.f_data.database_log)
        self.pool = None

    def init(self):
        global signal
        if self.f_data.sql_enabled:
            self.f_log.info("Initing SQL")
            sql_data = {
                "database": self.f_data.sql_db,
                "host": self.f_data.sql_host,
                "port": self.f_data.sql_port,
                "user": self.f_data.sql_user,
                "pass": self.f_data.sql_pass
                }
            for k, v in sql_data.items():
                if len(v) == 0:
                    self.f_log.error(f"Config error: value for {k} is empty")
                    signal = "empty"
                else:
                    signal = "valid"
            asyncio.run(self.start(signal))

    async def start(self, signal=None):
        if signal == "empty":
            self.f_log.warn("Received empty config flag. SQL will not start.")
            return
        if signal == "error":
            self.f_log.warn("Config error flag received. SQL will not start")
            return
        if signal == "valid" or signal is None:
            self.f_log.info("Starting PostgreSQL Pool")
            self.pool = await self.create_pool()

    async def create_pool(self):
        return await asyncpg.create_pool(
            f'postgresql://{self.f_data.sql_user}'
            f':{self.f_data.sql_pass}'
            f'@{self.f_data.sql_host}/'
            f'{self.f_data.sql_db}',
            min_size=0,
            max_size=5,
            max_queries=30,
            timeout=5,
            command_timeout=7,
            max_inactive_connection_lifetime=60
        )

    async def example_query(self, query):
        if self.pool is None:
            self.pool = await self.create_pool()
        async with self.pool.acquire() as connection:
            return await connection.fetch(query)
