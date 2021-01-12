import secrets
from configparser import ConfigParser
import os
from dotenv import load_dotenv
from pydantic import BaseSettings

config = ConfigParser()
config.read("config.ini")
load_dotenv()


class Settings(BaseSettings):
    SERVER_PORT: int = os.getenv("SERVER_PORT")
    SERVER_HOST: str = os.getenv("SERVER_HOST")

    SECRET_KEY: str = os.getenv("JWT_SECRET_KEY") or secrets.token_urlsafe(32)
    ALGORITHM = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    MYSQL_HOST: str = os.getenv("MYSQL_HOST")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE_NAME: str = os.getenv("MYSQL_DATABASE_NAME")
    SQLALCHEMY_DATABASE_URI: str = "mysql://%s:%s@%s/%s?charset=utf8" % (
        MYSQL_USER,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        MYSQL_DATABASE_NAME,
    )


settings = Settings()
