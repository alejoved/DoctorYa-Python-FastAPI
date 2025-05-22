import uuid
from sqlalchemy import UUID, Column, ForeignKey, String
from app.auth.entity.auth import Auth
from app.common.datasource import Base
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customer"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    auth_id = Column(String, ForeignKey(Auth.identification), unique=True)
    auth = relationship('Auth')