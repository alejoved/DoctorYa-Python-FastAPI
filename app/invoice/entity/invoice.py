import uuid
from sqlalchemy import UUID, Column, DateTime, Float, ForeignKey, String
from app.common.datasource import Base
from sqlalchemy.orm import relationship
from app.invoice_detail.entity.invoice_detail import InvoiceDetail

class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    code = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    total = Column(Float, nullable=False)

    details = relationship("InvoiceDetail", back_populates="invoice", cascade="all, delete-orphan")