from typing import Any, Optional

import uuid
from fastapi import APIRouter, Depends, HTTPException, Header, Response, Body
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.api import dependencies
from app.core.config import Settings
from app.schema import user as schema
from app import crud

router = APIRouter()


# 유저 정보 가져오기 - Token
@router.get("/", response_model=schema.User)
def get_user_info(
    db: Session = Depends(dependencies.get_db), user_agent: Optional[str] = Header(None)
) -> Any:
    return


# 유저 회원가입
@router.post("/register")
def register_user(
    db: Session = Depends(dependencies.get_db), *, user_in: schema.UserCreate
) -> Any:
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="This email already exists.")
    user = crud.user.create(db, obj_in=user_in)
    return Response(
        status_code=201,
    )


# 중복 이메일 체크
@router.post("/email-check")
def check_user_email() -> Any:
    return


# 유저 정보 수정 - Token
@router.put("/")
def update_user_info() -> Any:
    return


# 유저 탈퇴 - Token
@router.delete("/")
def delete_user_account() -> Any:
    return
