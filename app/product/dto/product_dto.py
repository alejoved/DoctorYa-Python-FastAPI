from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

class ProductDTO(BaseModel):
    id: Optional[UUID] = Field(description = "Primary ID", default=None)
    name: Optional[str] = Field(description = "Primary name for the product", default=None)
    description: Optional[str] = Field(description = "General product description", default=None)
    price: Optional[float] = Field(description = "Product price in dollars", default=None)
    tax: Optional[float] = Field(description = "Product tax in percentage", default=None)
    stock: Optional[int] = Field(description = "Product stock in quantity", default=None)


