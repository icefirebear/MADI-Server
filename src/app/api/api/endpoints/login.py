from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


# 기본정보로 로그인
@router.post("/login")
def login_general() -> Any:
    return


# access-token 으로 로그인
@router.post("/login/access-token")
def login_access_token() -> Any:
    return
