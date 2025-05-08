from pydantic import BaseModel

class PhysicianResponseDTO(BaseModel):
    name: str
    code: str
    speciality: str