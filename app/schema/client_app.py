from typing import Optional, List

from pydantic import BaseModel, HttpUrl

from .user import UserBase
from .authority import Authority

DEFAULT_APP_IMAGE = ""


class ClientAppBase(BaseModel):
    owner_uuid: Optional[str] = None
    app_id: Optional[str] = None
    secret_key: Optional[str] = None
    name: Optional[str] = None
    image: Optional[HttpUrl] = None
    redirect_uri: Optional[HttpUrl] = None
    approved_domain: Optional[List[HttpUrl]] = None
    authority: Optional[List[Authority]] = None


# API에서 ClientApp을 만들 때 필요한 정보
class ClientAppCreate(ClientAppBase):
    name: str
    image: HttpUrl = DEFAULT_APP_IMAGE
    redirect_uri: HttpUrl = None
    approved_domain: List[HttpUrl] = None
    authority: Optional[List[Authority]] = None


# API에서 ClientApp을 수정할 때 필요한 정보
class ClientAppUpdate(ClientAppCreate):
    pass


class ClientAppInDBBase(ClientAppBase):
    class Config:
        orm_mode = True


class ClientApp(ClientAppInDBBase):
    pass


class ClientAppInDB(ClientAppInDBBase):
    pass
