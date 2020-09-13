import logging
import os
from dotenv import load_dotenv

log = logging.getLogger()
log.setLevel(logging.DEBUG)
env = load_dotenv()

APP_PORT = os.getenv('APP_PORT')


class PostgresConfiguration:
    # POSTGRES_DB_PORT = os.getenv('POSTGRES_PORT')
    # POSTGRES_DB_NAME = os.getenv('POSTGRES_DB')
    # POSTGRES_DB_LOGIN = os.getenv('POSTGRES_USER')
    # POSTGRES_DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    # POSTGRES_DB_ADDRESS = os.getenv

    POSTGRES_DB_PORT = 5432
    POSTGRES_DB_NAME = 'fast_api_crud'
    POSTGRES_DB_LOGIN = 'postgres'
    POSTGRES_DB_PASSWORD = 'root'
    POSTGRES_DB_ADDRESS = 'localhost'

    @property
    def postgres_db_path(self):
        return f'postgres://{self.POSTGRES_DB_LOGIN}:{self.POSTGRES_DB_PASSWORD}@' \
               f'{self.POSTGRES_DB_ADDRESS}:' \
               f'{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB_NAME}'
