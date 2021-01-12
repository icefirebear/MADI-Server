from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
import random, string

from .base import CRUDBase
from app import crud
from app.model.client_app import ClientApp
from app.schema.client_app import ClientAppCreate, ClientAppUpdate


class CRUDClientApp(CRUDBase[ClientApp, ClientAppCreate, ClientAppUpdate]):
    def check_duplicate_id(self, db: Session, id):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, *, owner_uuid):
        return db.query(self.model).filter(self.model.owner_uuid == owner_uuid).all()

    def create(self, db, *, obj_in):
        random_id = "".join(random.choices(string.ascii_letters + string.digits, k=9))
        while self.check_duplicate_id(db, random_id):
            random_id = "".join(
                random.choices(string.ascii_letters + string.digits, k=9)
            )

        obj_in.id = random_id
        obj_in.secret_key = random.choices(string.ascii_letters + string.digits, k=20)
        app = super().create(db, obj_in)
        crud.authority.create_multi(app.id, obj_in.authority)

        return app


client_app = CRUDClientApp(ClientApp)
