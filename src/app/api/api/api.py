from fastapi import APIRouter

from .endpoints import oauth, user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["users"])
api_router.include_router(oauth.router, prefix="/oauth", tags=["oauth"])