from datetime import timedelta
from typing import Optional, Tuple
from model.user import User
from fastapi_sqlalchemy import db


class BaseAuthentication():

    def obtain_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        """
        그냥 jwt로 변환만 해줌 (토큰 발급)
        Returns: token
        """
        return
