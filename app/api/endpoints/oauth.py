from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_sqlalchemy import db

from app import crud, model
from app.api import dependencies
from app.schema.client_app import ClientAppCreate, ClientAppUpdate

router = APIRouter()


# access_token 발행하기
@router.get("/authorize")
async def issue_access_token(
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
) -> Any:
    return


@router.get("/access-token")
async def verify_access_token(
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
) -> Any:
    return


# OAuth  목록 가져오기 - Token
@router.get("/")
async def get_app_list(
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
) -> Any:
    my_apps = crud.client_app.get_multi(db)
    return my_apps


@router.get("/{app_id}")
async def get_app_info(
    app_id: str,
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
):
    return crud.client_app.get(app_id)


# OAuth 클라이언트 생성 - Token
@router.post("/")
async def create_app(
    user_in: ClientAppCreate,
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
):
    user_in.owner_uuid = current_user.uuid
    return crud.client_app.create(db, user_in)


@router.put("/{app_id}")
async def update_app(
    app_id: str,
    user_in: ClientAppUpdate,
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
):
    app = crud.client_app.get(user_in.id)
    if app.owner_uuid != current_user.uuid:
        raise HTTPException(status_code=403, detail="Forbidden")

    user_in.id = app_id
    return crud.client_app.update(user_in)


# OAuth 클라이언트 삭제
@router.delete("/{app_id}")
async def delete_app(
    app_id: str,
    db: Session = Depends(dependencies.get_db),
    current_user: model.User = Depends(dependencies.get_current_user),
):
    app = crud.client_app.get(user_in.id)
    if app.owner_uuid != current_user.uuid:
        raise HTTPException(status_code=403, detail="Forbidden")

    return crud.client_app.remove(app_id, current_user.uuid)
