from typing import List
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .base import CRUDBase
from app.model.approved_domain import ApprovedDomain


class CRUDApprovedDomain(CRUDBase[ApprovedDomain, BaseModel, BaseModel]):
    def create_multi(self, db: Session, *, app_id, domains):
        db_objs = [ApprovedDomain(domain=domain, app_id=app_id) for domain in domains]

        db.add_all(db_objs)
        db.commit()

    def update_multi(self, db: Session, *, app_id, domains: List[str]):
        self.delete(db, app_id=app_id)
        self.create_multi(db, app_id=app_id, domains=domains)

    def delete(self, db: Session, *, app_id):
        domains = db.query(self.model).filter(self.model.app_id == app_id).all()

        for domain in domains:
            db.delete(domain)
        db.commit()


approved_domain = CRUDApprovedDomain(ApprovedDomain)
