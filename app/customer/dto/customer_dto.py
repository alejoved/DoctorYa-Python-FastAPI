from pydantic import BaseModel, Field
from app.customer.entity.customer import Customer

class CustomerDTO(BaseModel):
    identification: str = Field(description = "Primary identification for the customer")
    password: str = Field(description = "Password for the login")
    name: str = Field(description = "Customer full name")
    insurance: str = Field(description = "Name of the health insurance")
