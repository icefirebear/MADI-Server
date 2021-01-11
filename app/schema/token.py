from typing import Optional
from enum import Enum

from pydantic import BaseModel, EmailStr, HttpUrl


class Token(BaseModel):
    token: str


class TokenPayload(BaseModel):
    email: str
    std_no: str
    name: str
