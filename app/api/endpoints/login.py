from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from app.core.config import settings
from app.schema.user import UserLogin
from app.schema.token import Token
from app.api import dependencies
from app.core.security import obtain_token
from app import crud

router = APIRouter()


# 기본정보로 로그인
@router.post("/", response_model=Token)
def login_by_general(
        db: Session = Depends(dependencies.get_db), form_data: UserLogin = Body(...)
) -> Any:
    user = crud.user.authenticate(
        db, email=form_data.email, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": user.email,
        "std_no": user.std_no,
        "name": user.name,
        "gender": user.gender.value
    }

    return {"token": obtain_token(payload=payload, expires_delta=access_token_expires)}
