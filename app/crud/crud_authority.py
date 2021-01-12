from typing import List
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .base import CRUDBase
from app.model.authority import Authority
from app.schema.authority import Authority as AuthorityEnum


class CRUDAuthority(CRUDBase[Authority, BaseModel, BaseModel]):
    def create_multi(self, db: Session, *, app_id, authorities: List[AuthorityEnum]):
        db_objs = [
            Authority(authority=authority.value, app_id=app_id)
            for authority in authorities
        ]

        db.add_all(db_objs)
        db.commit()

    def update_multi(self, db: Session, *, app_id, authorities: List[AuthorityEnum]):
        self.delete(db, app_id=app_id)
        self.create_multi(db, app_id=app_id, authorities=authorities)

    def delete(self, db: Session, *, app_id):
        authorities = db.query(self.model).filter(self.model.app_id == app_id).all()

        for authority in authorities:
            db.delete(authority)
        db.commit()


authority = CRUDAuthority(Authority)
