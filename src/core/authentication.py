import jwt

from datetime import datetime, timedelta
from typing import Optional, Tuple

from app import config
from model import User
from .base_authentication import BaseAuthentication

SECRET_KEY = config.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class JWTAuthentication(BaseAuthentication):

    def authenticate(self, email, password) -> Tuple[User,str]:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

