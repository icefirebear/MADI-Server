from typing import Any, Optional

import re
from fastapi import APIRouter, Depends, HTTPException, Header, Response, Body
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr

from app.api import dependencies
from app.core.config import Settings
from app.schema import user as schema
from app import crud, model

router = APIRouter()


# 유저 정보 가져오기 - Token
@router.get("/", response_model=schema.User)
def get_user_info(
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
) -> Any:
    return current_user


# 유저 회원가입
@router.post("/register")
def register_user(
    db: Session = Depends(dependencies.get_db), *, user_in: schema.UserCreate
) -> Any:
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="This email already exists.")
    user = crud.user.create(db, obj_in=user_in)
    return Response(status_code=201)


# 중복 이메일 체크
@router.post("/email-check")
def check_user_email(
    db: Session = Depends(dependencies.get_db), email: EmailStr = None
) -> Any:

    # 이메일 형식검사
    p = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if not p.match(email) != None:
        raise HTTPException(status_code=422, detail="invalid email format")
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(status_code=400, detail="This email already exists.")
    return Response(status_code=200)


# 유저 정보 수정 - Token
@router.put("/", response_model=schema.User)
def update_user_info(
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
    *,
    user_in: schema.UserUpdate
) -> Any:
    user = crud.user.update(db, current_user, user_in)
    return user


# 유저 탈퇴 - Token
@router.delete("/")
def delete_user_account(
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
) -> Any:
    user = crud.user.remove(db, current_user)
    return Response(status_code=204)
