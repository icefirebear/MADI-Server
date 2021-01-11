from crud.base import CRUDBase
from model.cilent_app import ClientApp
from schema.client_app import ClientAppCreate, ClientAppUpdate


class CRUDClientApp(CRUDBase[ClientApp, ClientAppCreate, ClientAppUpdate]):
    def get_multi(self, db: Session, *, id):
        pass


client_app = CRUDClientApp(ClientApp)
