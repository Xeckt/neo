import asyncpg
import handler.config.data
import handler.logging.foxlog


class Sql:

    def __init__(self):
        self.foxcord_data = handler.config.data.FoxcordData()
        self.foxlog = handler.logging.foxlog.Log().create_logger(__name__, self.foxcord_data.database_log)
        self.pool = None

    async def start(self):
        self.foxlog.info("Starting PostgreSQL Pool")
        await self.create_pool()

    async def create_pool(self):
        return await asyncpg.create_pool(
            f'postgresql://{self.foxcord_data.database_user}'
            f':{self.foxcord_data.database_password}'
            f'@{self.foxcord_data.database_host}/'
            f'{self.foxcord_data.database_name}',
            min_size=0,
            max_size=5,
            max_queries=30,
            timeout=5,
            command_timeout=7,
            max_inactive_connection_lifetime=60
        )

    async def example_query(self, query):
        if self.pool is None: # If the pool isn't spawned when running query, create one
            self.pool = await self.create_pool()
        async with self.pool.acquire() as connection: # Acquire a pool resource and fetch a query against the DB
            return await connection.fetch(query) # Return the value for manipulation
