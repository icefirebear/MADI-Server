from sqlalchemy import Table, Column, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from .base import Base
from .client_app import ClientApp


class ApprovedDomain(Base):
    domain = Column(String(255), primary_key=True)
    app_id = Column(
        String(9), ForeignKey("clientapp.app_id", ondelete="CASCADE"), primary_key=True
    )

    app = relationship("ClientApp", back_populates="approved_domain")
