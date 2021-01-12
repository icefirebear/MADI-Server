import uvicorn
from configparser import ConfigParser
from app.core.config import settings


def main():
    config = ConfigParser()
    config.read("./config.ini")

    PORT = settings.SERVER_PORT
    HOST = settings.SERVER_HOST

    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)


if __name__ == "__main__":
    main()
