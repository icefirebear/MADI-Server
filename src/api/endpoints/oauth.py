from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_sqlalchemy import db

from src import crud

router = APIRouter()


# access_token 받아오기
@router.get("/authorize")
async def issue_access_token(db: Session = Depends(db.session)) -> Any:
    return


@router.get("/access-token")
async def verify_access_token(db: Session = Depends(db.session)) -> Any:
    return


# OAuth  목록 가져오기 - Token
@router.get("/")
async def get_app_list(db: Session = Depends(db.session)) -> Any:
    my_apps = crud.client_app.get_multi(db)
    return my_apps


@router.get("/")
async def get_app_info(db: Session = Depends(db.session)):
    return


# OAuth 클라이언트 생성 - Token
@router.post("/")
async def create_app(db: Session = Depends(db.session)):
    return


@router.put("/")
async def update_app(db: Session = Depends(db.session)):
    return


# OAuth 클라이언트 삭제
@router.delete("/")
async def delete_app(db: Session = Depends(db.session)):
    return
