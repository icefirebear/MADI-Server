from sqlalchemy import Table, Column, Integer, String, DateTime, Text, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from pytz import timezone

from .base import Base

from app.schema.authority import Authority as AuthEnum


class Authority(Base):
    authority = Column(Enum(AuthEnum), primary_key=True)
    app_id = Column(String(36), primary_key=True)

    app = relationship("ClientApp", back_populates="authorities")
