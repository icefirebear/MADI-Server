from datetime import timedelta
from typing import Optional, Tuple


class BaseAuthentication():

    def authenticate(self, email, password) -> Tuple[None,str]:
        """
        email과 password의 유효성 검사와 login 처리 (토큰 발급)
        Returns: (User , token)
        """