from sqlalchemy import Table, Column, Integer, String, DateTime, Text, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from pytz import timezone

from .base import Base
from app.schema.user import Gender, DEFAULT_PROFILE_IMAGE


class User(Base):
    uuid = Column(String(36), primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    std_no = Column(String(4), nullable=False)
    name = Column(String(45), nullable=False)
    gender = Column(Enum(Gender), default=Gender.none)
    profile_image = Column(Text, default=DEFAULT_PROFILE_IMAGE)
    std_no_updated_at = Column(DateTime, default=datetime.now(timezone("Asia/Seoul")))

    client_apps = relationship("ClientApp", back_populates="owner")
