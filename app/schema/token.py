from typing import Optional
from enum import Enum
from datetime import datetime

from pydantic import BaseModel, EmailStr, HttpUrl


class Token(BaseModel):
    token: str


class TokenPayload(BaseModel):
    exp: datetime
    sub: str
    std_no: str
    name: str
