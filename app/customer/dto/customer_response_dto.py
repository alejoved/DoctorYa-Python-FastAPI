from typing import Optional
from pydantic import BaseModel, Field
from app.auth.dto.auth_response_dto import AuthResponseDTO
from app.customer.entity.customer import Customer

class CustomerResponseDTO(BaseModel):
    name: Optional[str] = Field(default = None, description = "Customer full name")
    address: Optional[str] = Field(default = None, description = "Customer full address")
    auth: Optional[AuthResponseDTO] = Field(default = None, description = "Authentication data of the customer")