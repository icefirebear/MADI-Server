import pytest

from typing import Generator
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture()
def token_headers() -> dict:
    # 나중에 헤더 얻는 코드 작성
    return {"Authorization": "asdasf.agagd.gsgdsg"}


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as c:
        yield c
