from pydantic import BaseModel
from app.physician.entity.physician import Physician


class PhysicianResponseDTO(BaseModel):
    name: str
    code: str
    speciality: str

def physician_to_dto(physician: Physician):
    return PhysicianResponseDTO(
        name = physician.name,
        code = physician.code,
        speciality = physician.speciality
    )