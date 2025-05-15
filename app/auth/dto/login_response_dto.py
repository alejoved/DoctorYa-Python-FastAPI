from typing import Optional
from pydantic import BaseModel, Field
from app.common.role import Role

class LoginResponseDTO(BaseModel):
    token: Optional[str] = Field(description="JWT Token encrypt")
    role: Optional[Role] = Field(description="Role admin, patient, physician", example="ADMIN")

