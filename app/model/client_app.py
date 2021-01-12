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


class ClientApp(Base):
    app_id = Column(String(9), primary_key=True)
    owner_uuid = Column(String(36), ForeignKey("user.uuid"))
    secret_key = Column(String(255), nullable=False)
    name = Column(String(45), nullable=False)
    image = Column(Text, default=DEFAULT_APP_IMAGE)
    redirect_uri = Column(String(45), nullable=False)

    owner = relationship("User", back_populates="client_apps")
    authorities = relationship("Authority", back_populates="app")
    approved_domain = relationship("ApprovedDomain", back_populates="app")
