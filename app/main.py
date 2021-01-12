from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI()


@app.get("/")
async def test():
    return {"message": "Hello FastAPI"}


app.include_router(api_router)
