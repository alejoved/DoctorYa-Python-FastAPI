from pydantic import BaseModel, Field

class LoginDTO(BaseModel):
    identification: str = Field(description="Identification for the login")
    password: str = Field(min_length=4, description="Password for the login minimum 4 characters")
    