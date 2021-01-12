from sqlalchemy import Table, Column, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .client_app import ClientApp

from app.schema.authority import Authority as AuthEnum


class Authority(Base):
    authority = Column(Enum(AuthEnum), primary_key=True)
    app_id = Column(
        String(9), ForeignKey("clientapp.app_id", ondelete="CASCADE"), primary_key=True
    )

    app = relationship("ClientApp", back_populates="authorities")
