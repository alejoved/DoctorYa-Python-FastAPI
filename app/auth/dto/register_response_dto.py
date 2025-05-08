from pydantic import BaseModel

from app.auth.entity.auth import Auth


class RegisterResponseDTO(BaseModel):
    identification: str