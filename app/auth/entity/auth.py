import uuid
from sqlalchemy import UUID, Column, String, Enum as SqlEnum
from app.common.datasource import Base
from app.common.role import Role

class Auth(Base):
    __tablename__ = "auth"

    identification = Column(String, primary_key=True, index=True)
    password = Column(String)
    role = Column(SqlEnum(Role), nullable=False)