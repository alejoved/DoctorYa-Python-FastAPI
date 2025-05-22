from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_serializer
from app.product.dto.product_dto import ProductDTO

class InvoiceDetailDTO(BaseModel):
    quantity: int = Field(description="Product quantity")
    subtotal_tax : Optional[float] = Field(description="Product subtotal tax", default=None)
    subtotal : Optional[float] = Field(description="Product subtotal", default=None)
    product: ProductDTO = Field(description="Product full data")
    