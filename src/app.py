from fastapi import FastAPI
from configparser import ConfigParser

config = ConfigParser()
config.read("../config.ini")

app = FastAPI()


@app.get("/")
async def test():
    return {"message": "Hello FastAPI"}
