from pydantic import BaseModel
from app.physician.entity.physician import Physician

class PhysicianDTO(BaseModel):
    identification: str
    password: str
    name: str
    code: str
    speciality: str


