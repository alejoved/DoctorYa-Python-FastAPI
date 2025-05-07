import uuid
from sqlalchemy import UUID, Column, String
from app.common.datasource import Base

class Patient(Base):
    __tablename__ = "patient"
    __table_args__ = {"schema": "doctoryapython"}


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    insurance = Column(String)