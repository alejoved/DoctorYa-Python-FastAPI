import uuid
from sqlalchemy import UUID, Column, String
from app.common.datasource import Base

class Physician(Base):
    __tablename__ = "physician"
    __table_args__ = {"schema": "doctoryapython"}


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    code = Column(String)
    speciality = Column(String)