from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session

from .base import CRUDBase
from app.model.client_app import ClientApp
from app.schema.client_app import ClientAppCreate, ClientAppUpdate


class CRUDClientApp(CRUDBase[ClientApp, ClientAppCreate, ClientAppUpdate]):
    def get_multi(self, db: Session, *, id):
        return db.query(self.model).filter(self.model.owner_uuid == id).all()

    def create(self, db: Session, *, obj_in: ClientAppCreate):
        db_obj = ClientApp()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: User,
        obj_in: Union[ClientAppUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


client_app = CRUDClientApp(ClientApp)
