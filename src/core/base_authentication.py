from datetime import timedelta
from typing import Optional, Tuple
from model.user import User

class BaseAuthentication():

    def authenticate(self, email, password) -> Tuple[User,str]:
        """
        email과 password의 유효성 검사와 login 처리 (토큰 발급)
        Returns: (User , token)
        """