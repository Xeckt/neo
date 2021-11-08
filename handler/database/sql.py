import handler.config.data
import handler.logging.foxlog
import mysql.connector.pooling


class Sql:
    foxcord_data = handler.config.data.FoxcordData
    foxlog = handler.logging.foxlog.Log().create_logger(__name__, foxcord_data.database_log)

    def __init__(self):
        self.pool = None
        self.pool_size = 5

    def start(self):
        self.create_pool()

    def create_pool(self):
        self.pool = mysql.connector.connect(pool_name = 'foxcord',
                                            pool_size=self.pool_size,
                                            database=self.foxcord_data.database_name,
                                            host=self.foxcord_data.database_host,
                                            port=self.foxcord_data.database_port,
                                            user=self.foxcord_data.database_user,
                                            password=self.foxcord_data.database_password,
                                            charset='utf8mb4')

    def example_query(self):
        query = "SELECT * FROM *" # Set your query
        cursor = self.pool.cursor(buffered=True) # Instantiate a cursor with the instanced pool object
        cursor.execute(query) # execute the query on the database once you have a cursor
        # https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html



