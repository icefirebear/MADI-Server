from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Boolean,
    Enum,
    ForeignKey,
    ForeignKeyConstraint,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base
from app.schema.client_app import DEFAULT_APP_IMAGE

from app.schema.authority import Authority as AuthEnum
from .authority import Authority


class ClientApp(Base):
    uuid = Column(String(36), primary_key=True)
    owner_uuid = Column(String(36), ForeignKey("user.uuid"))
    id = Column(String(9), nullable=False)
    secret_key = Column(String(255), nullable=False)
    name = Column(String(45), nullable=False)
    image = Column(Text, default=DEFAULT_APP_IMAGE)
    redirect_uri = Column(String(45), nullable=False)

    owner = relationship("User", back_populates="client_apps")
    authorities = relationship("Authority", back_populates="app")

    authoritiy_authority = Column(Enum(AuthEnum))
    authoritiy_app_id = Column(String(36))

    __table_args__ = (
        ForeignKeyConstraint(
            [authoritiy_authority, authoritiy_app_id],
            [Authority.authority, Authority.app_id],
        ),
        {},
    )
