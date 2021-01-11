from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session

from .base import CRUDBase
from app.model.client_app import ClientApp
from app.schema.client_app import ClientAppCreate, ClientAppUpdate


class CRUDClientApp(CRUDBase[ClientApp, ClientAppCreate, ClientAppUpdate]):
    def get_multi(self, db: Session, *, id):
        return db.query(self.model).filter(self.model.owner_uuid == id).all()


client_app = CRUDClientApp(ClientApp)
