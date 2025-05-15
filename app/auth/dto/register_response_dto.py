from typing import Optional
from pydantic import BaseModel, Field

class RegisterResponseDTO(BaseModel):
    identification: Optional[str] = Field(min_length= 4, description = "Primary identification for the sign up")