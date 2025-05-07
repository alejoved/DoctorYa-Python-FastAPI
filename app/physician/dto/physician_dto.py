from pydantic import BaseModel
from app.physician.entity.physician import Physician

class PhysicianDTO(BaseModel):
    identification: str
    password: str
    name: str
    code: str
    speciality: str

def dto_to_physician(physician_dto: PhysicianDTO):
    return Physician(
        name = physician_dto.name,
        code = physician_dto.code,
        speciality = physician_dto.speciality
    )