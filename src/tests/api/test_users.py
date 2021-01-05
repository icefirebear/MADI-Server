import re

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


BASE_URL = "http://localhost:8000"

MOCK_USERS = {
    "correct_user": {
        "email": "student1@example.com",
        "password": "1234",
        "name": "학생1",
        "stdNo": 2217,
        "sex": "male",
    }
}


def test_create_user(client: TestClient) -> None:
    data = MOCK_USERS["correct_user"]
    response = client.post(f"{BASE_URL}/user/register", json=data)

    assert 201 == response.status_code


def test_login_user(client: TestClient) -> None:
    data = {
        "email": MOCK_USERS["correct_user"]["email"],
        "password": MOCK_USERS["correct_user"]["password"],
    }
    response = client.post(f"{BASE_URL}/user/register", json=data)

    assert 200 == response.status_code
    token_regular = re.compile("\B[.]\B[.]\B")
    assert token_regular.match(response.json()["token"])
