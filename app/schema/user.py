from typing import Optional
from enum import Enum

from pydantic import BaseModel, EmailStr, HttpUrl

DEFAULT_PROFILE_IMAGE = "https://cdn.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png"


class Gender(Enum):
    male = 1
    female = 2
    none = 3


# User의 공유 속성
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    std_no: Optional[str] = None
    name: Optional[str] = None
    gender: Optional[Gender] = None
    profile_image: Optional[HttpUrl] = None


# API에서 User 생성시 받을 정보
class UserCreate(UserBase):
    email: EmailStr
    password: str
    std_no: str
    name: str
    gender: Gender
    profile_image: Optional[HttpUrl] = DEFAULT_PROFILE_IMAGE


# Login시 받을 정보
class UserLogin(UserBase):
    email: EmailStr
    password: str


# API에서 User 수정시 받을 정보
class UserPasswordUpdate(UserBase):
    password: Optional[str]


# API에서 User 수정시 받을 정보
class UserUpdate(UserBase):
    name: str
    std_no: str
    gender: Gender
    profile_image: Optional[HttpUrl] = DEFAULT_PROFILE_IMAGE


class UserInDBBase(UserBase):
    uuid: Optional[str]

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hased_password: str
