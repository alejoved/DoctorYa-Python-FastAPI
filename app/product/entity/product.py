import uuid
from sqlalchemy import UUID, Column, Float, Integer, String
from app.auth.entity.auth import Auth
from app.common.datasource import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)