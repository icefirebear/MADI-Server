from sqlalchemy.orm import Session
from pydantic import BaseModel

from .base import CRUDBase
from app.model.authority import Authority
from app.schema.authority import Authority as AuthorityEnum


class CRUDAuthority(CRUDBase[Authority, BaseModel, BaseModel]):
    def create_multi(self, db: Session, *, app_id, authorities):
        db_objs = [
            Authority(authority=AuthorityEnum[authority], app_id=app_id)
            for authority in authorities
            if AuthorityEnum[authority]
        ]

        db.add_all(db_objs)


authority = CRUDAuthority(Authority)
