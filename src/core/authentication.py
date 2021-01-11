from jose import jwt

from datetime import datetime, timedelta
from typing import Optional, Tuple


from passlib.context import CryptContext
from app import config
from model import User
from crud import crud_user
from .base_authentication import BaseAuthentication

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = config.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_password_hash(password : str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password : str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

class JWTAuthentication(BaseAuthentication):

    def authenticate(self,data, expires_delta : Optional[datetime]) -> Tuple[User,str]:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

