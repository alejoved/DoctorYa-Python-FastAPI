from pydantic import BaseModel
from app.common.role import Role

class LoginResponseDTO(BaseModel):
    token: str
    role: Role

