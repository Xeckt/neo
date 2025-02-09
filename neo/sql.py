import asyncpg
import globals
from log import Log

class Sql:
    def __init__(self):
        self.pool = None
        self.log = Log().create(__name__, globals.neo_config.databaseLog)
        self.loaded = False

    async def start(self, signal=None):
        if signal == "valid" or signal is None:
            self.log.info("Starting PostgreSQL Pool")
            self.pool = await self.create_pool()
            self.loaded = True
            self.log.debug(f"postgres pool: {self.pool}")

    async def create_pool(self):
        return await asyncpg.create_pool(
            f'postgresql://{globals.neo_config.sql_user}'
            f':{globals.neo_config.sql_pass}'
            f'@{globals.neo_config.sql_host}/'
            f'{globals.neo_config.sql_db}',
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

    async def send_transaction(self):
        async with self.pool.acquire as connection:
            async with connection.transaction():
                await connection.execute("TRANSACTION_QUERY")
