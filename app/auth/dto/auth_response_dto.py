from pydantic import BaseModel

class AuthResponseDTO(BaseModel):
    identification: str