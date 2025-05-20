from pydantic import BaseModel, Field
from app.product.entity.product import Product

class ProductDTO(BaseModel):
    identification: str = Field(description = "Primary identification for the product")
    password: str = Field(description = "Password for the log in")
    name: str = Field(description = "Product full name")
    code: str = Field(description = "General medical code")
    speciality: str = Field(description = "Speciality field of the product")


