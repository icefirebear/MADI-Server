from fastapi import FastAPI
from configparser import ConfigParser

from middleware import DBSession

config = ConfigParser()
config.read("config.ini")

app = FastAPI()

app.add_middleware(DBSession, db_url=config.get("default", "DB_URL"))


@app.get("/")
async def test():
    return {"message": "Hello FastAPI"}
