from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

router = APIRouter()


# 유저 정보 가져오기 - Token
@router.get('/')
def get_user_info() -> Any:
    return


# 유저 회원가입
@router.post('/register')
def register_user() -> Any:
    return


# 중복 이메일 체크
@router.post('/email-check')
def check_user_email() -> Any:
    return


# 유저 정보 수정 - Token
@router.put('/')
def update_user_info() -> Any:
    return


# 유저 탈퇴 - Token
@router.delete('/')
def delete_user_account() -> Any:
    return

