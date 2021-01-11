import re
import pytest
from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


BASE_URL = "http://localhost:5000"


def test_get_oauth_client_list(
    client: TestClient, token_headers: Dict[str, str]
) -> None:
    pass


def test_get_access_token_by_client_id(client: TestClient) -> None:
    pass


def test_create_client(client: TestClient, token_headers: Dict[str, str]) -> None:
    pass


def test_delete_client(client: TestClient, token_headers: Dict[str, str]) -> None:
    pass
