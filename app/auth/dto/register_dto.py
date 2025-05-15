from pydantic import BaseModel, Field

class RegisterDTO(BaseModel):
    identification: str = Field(description = "Primary identification for the sign up")
    password: str = Field(min_length= 4, description = "Password for the sign up")