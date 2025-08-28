import os
import json
import logging
from dotenv import load_dotenv

load_dotenv(verbose=True)

logger = logging.getLogger(__name__)

class Environment:
    """Helper class to get environment variables"""

    @classmethod
    def get_string(cls, config_name, default=""):
        return str(os.getenv(config_name, default))

    @classmethod
    def get_int(cls, config_name, default=0):
        return int(os.getenv(config_name, default))

    @classmethod
    def get_string_list(cls, config_name, default=[]):
        string = cls.get_string(config_name)
        if string == "":
            return default
        return list(map(lambda x: x.strip(), str(string).split(",")))

    @classmethod
    def get_bool(cls, config_name):
        return os.getenv(config_name) == "true" or os.getenv(config_name) == "True"



class Config:
    name = Environment.get_string("APP_NAME", "FastApi Template")
    host = Environment.get_string("APP_HOST", "0.0.0.0")
    port = Environment.get_int("APP_PORT", 8000)
    log_level = Environment.get_string("APP_LOG_LEVEL", "DEBUG").upper()
    is_development = Environment.get_string("ENVIRONMENT") == "DEVELOPMENT"
    root_path = Environment.get_string("APP_ROOT_PATH", "")
    if root_path != "":
        root_path = f"/{root_path}"

    postgres_user = Environment.get_string("POSTGRES_USER", "")
    postgres_password = Environment.get_string("POSTGRES_PASSWORD","")
    postgres_db = Environment.get_string("POSTGRES_DB", "")
    postgres_host = Environment.get_string("POSTGRES_HOST", "")
    postgres_port = Environment.get_int("POSTGRES_PORT", 5432)

    async_db_uri = "postgresql+asyncpg://" + postgres_user + ":" + postgres_password + "@" + postgres_host + ":" + str(postgres_port) + "/" + postgres_db
    sync_db_uri = "postgresql+psycopg2://" + postgres_user + ":" + postgres_password + "@" + postgres_host + ":" + str(postgres_port) + "/" + postgres_db    