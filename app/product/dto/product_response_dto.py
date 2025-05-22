from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

from app.auth.dto.auth_response_dto import AuthResponseDTO

class ProductResponseDTO(BaseModel):
    id: Optional[UUID] = Field(default = None, description = "Product ID")
    name: Optional[str] = Field(default = None, description = "Product full name")
    description: Optional[str] = Field(default = None, description = "General product description")
    price: Optional[float] = Field(default = None, description = "Product price in dollars")
    tax: Optional[float] = Field(default = None, description = "Product tax in percentage")
    stock: Optional[int] = Field(default = None, description = "Product stock in quantity")