from pydantic import BaseModel

from app.auth.entity.auth import Auth

class RegisterDTO(BaseModel):
    identification: str
    password: str