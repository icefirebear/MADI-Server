from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
import random, string

from .base import CRUDBase
from app import crud, model
from app.model.client_app import ClientApp
from app.schema.client_app import ClientAppCreate, ClientAppUpdate, ClientAppInDB


class CRUDClientApp(CRUDBase[ClientApp, ClientAppCreate, ClientAppUpdate]):
    def check_duplicate_id(self, db: Session, app_id):
        return db.query(self.model).filter(self.model.app_id == app_id).first()

    def get(self, db: Session, *, app_id):
        app = db.query(self.model).filter(self.model.app_id == app_id).first()
        app.authority = [
            item.authority.value
            for item in (
                db.query(model.Authority).filter(model.Authority.app_id == app_id).all()
            )
        ]
        app.approved_domain = [
            item.domain
            for item in (
                db.query(model.ApprovedDomain)
                .filter(model.ApprovedDomain.app_id == app_id)
                .all()
            )
        ]

        return app

    def get_multi(self, db: Session, *, owner_uuid):
        app_ids = (
            db.query(self.model.app_id)
            .filter(self.model.owner_uuid == owner_uuid)
            .all()
        )
        return [self.get(db, app_id=app_id) for app_id in app_ids]

    def create(self, db: Session, *, obj_in: ClientAppCreate):
        random_id = "".join(random.choices(string.ascii_letters + string.digits, k=9))
        while self.check_duplicate_id(db, random_id):
            random_id = "".join(
                random.choices(string.ascii_letters + string.digits, k=9)
            )
        obj_in.app_id = random_id
        obj_in.secret_key = "".join(
            random.choices(string.ascii_letters + string.digits, k=20)
        )

        app = ClientApp(
            app_id=obj_in.app_id,
            owner_uuid=obj_in.owner_uuid,
            secret_key=obj_in.secret_key,
            name=obj_in.name,
            image=str(obj_in.image),
            redirect_uri=str(obj_in.redirect_uri),
        )

        db.add(app)
        db.commit()
        db.refresh(app)

        crud.authority.create_multi(
            db, app_id=obj_in.app_id, authorities=obj_in.authority
        )
        crud.approved_domain.create_multi(
            db, app_id=obj_in.app_id, domains=obj_in.approved_domain
        )

        return obj_in

    def update(self, db: Session, *, db_obj: ClientApp, obj_in: ClientAppUpdate):
        super().update(db, db_obj=db_obj, obj_in=obj_in)
        crud.authority.update_multi(
            db, app_id=db_obj.app_id, authorities=obj_in.authority
        )
        crud.approved_domain.update_multi(
            db, app_id=db_obj.app_id, domains=obj_in.approved_domain
        )

        return self.get(db, app_id=db_obj.app_id)


client_app = CRUDClientApp(ClientApp)
