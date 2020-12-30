import uvicorn

from app import app
from configparser import ConfigParser


def main():
    config = ConfigParser()
    config.read("../config.ini")

    try:
        PORT: int = int(config.get("default", "PORT"))
    except Exception as e:
        PORT: int = 5000

    uvicorn.run("app:app", port=PORT, reload=True)


if __name__ == "__main__":
    main()
