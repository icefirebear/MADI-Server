from base64 import b64decode
from typing import Generator

from fastapi import Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer

import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, model, schema
from app.core.config import settings
from app.db.session import LocalSession

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="login")


def get_db() -> Generator:
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), authorization: str = Header(None)
) -> model.User:

    try:
        if authorization.split()[0] not in ("jwt", "JWT"):
            raise HTTPException(400, "credentials required")
        token = authorization.split()[1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        token_data = schema.token.TokenPayload(**payload)
    except (ValidationError) as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, email=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
