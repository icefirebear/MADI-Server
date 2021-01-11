from fastapi import FastAPI
from configparser import ConfigParser

from app.api.api import api_router
from app.middleware import DBSession

config = ConfigParser()
config.read("config.ini")

app = FastAPI()

app.add_middleware(DBSession, db_url=config.get("default", "DB_URL"))


@app.get("/")
async def test():
    return {"message": "Hello FastAPI"}


app.include_router(api_router)
