from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_serializer
from app.product.dto.product_response_dto import ProductResponseDTO

class InvoiceDetailResponseDTO(BaseModel):
    quantity: Optional[int] = Field(default=None, description="Product quantity")
    subtotal_tax: Optional[float] = Field(default=None, description="Invoice detail total tax")
    subtotal: Optional[float] = Field(default=None, description="Invoice detail subtotal")
    product: ProductResponseDTO = Field(default=None, description="Product full data")