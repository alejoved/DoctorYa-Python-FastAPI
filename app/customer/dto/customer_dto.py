from pydantic import BaseModel, Field
from app.customer.entity.customer import Customer

class CustomerDTO(BaseModel):
    identification: str = Field(description = "Primary identification for the customer")
    name: str = Field(description = "Customer full name")
    password: str = Field(description = "Password for the login")
    address: str = Field(description = "Customer full address")
