from sqlalchemy.orm import Session
from pydantic import BaseModel

from .base import CRUDBase
from app.model.approved_domain import ApprovedDomain


class CRUDApprovedDomain(CRUDBase[ApprovedDomain, BaseModel, BaseModel]):
    def create_multi(self, db: Session, *, app_id, domains):
        db_objs = [ApprovedDomain(domain=domain, app_id=app_id) for domain in domains]

        db.add_all(db_objs)
        db.commit()


approved_domain = CRUDApprovedDomain(ApprovedDomain)
