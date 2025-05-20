from typing import Optional
from pydantic import BaseModel, Field

from app.auth.dto.auth_response_dto import AuthResponseDTO

class ProductResponseDTO(BaseModel):
    name: Optional[str] = Field(default = None, description = "Product full name")
    code: Optional[str] = Field(default = None, description = "General medical code")
    speciality: Optional[str] = Field(default = None, description = "Speciality field of the product")
    auth: Optional[AuthResponseDTO] = Field(default = None, description = "Authentication data of the product")