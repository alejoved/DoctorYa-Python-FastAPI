from typing import Optional
from pydantic import BaseModel, Field

class AuthResponseDTO(BaseModel):
    identification: Optional[str] = Field(default = None, description="Primary identification for the admin, patient, physician")