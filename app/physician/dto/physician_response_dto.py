from pydantic import BaseModel

from app.auth.dto.auth_response_dto import AuthResponseDTO

class PhysicianResponseDTO(BaseModel):
    name: str
    code: str
    speciality: str
    auth: AuthResponseDTO