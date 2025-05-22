import uuid
from sqlalchemy import UUID, Column, Float, ForeignKey, Integer, String
from app.common.datasource import Base
from sqlalchemy.orm import relationship

class InvoiceDetail(Base):
    __tablename__ = "invoice_detail"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    quantity = Column(Integer, nullable=False)
    subtotal_tax = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"))
    product = relationship('Product')
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoice.id"))
    invoice = relationship("Invoice", back_populates="details")