from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import settings
from app.schema.user import UserLogin, Token
from app.api import dependencies
from app.core.authentication import JWTAuthentication
from app import crud

router = APIRouter()


# 기본정보로 로그인
@router.post("/", response_model=Token)
def login_by_general(
    db: Session = Depends(dependencies.get_db), form_data: UserLogin = Depends()
) -> Any:
    user = crud.user.authenticate(
        db, email=form_data.email, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minute=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "token": JWTAuthentication.obtain_token(
            user.email, expires_delta=access_token_expires
        )
    }


# access-token 으로 로그인
@router.get("/access-token")
def login_by_access_token() -> Any:
    return
