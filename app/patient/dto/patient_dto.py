from pydantic import BaseModel
from app.patient.entity.patient import Patient

class PatientDTO(BaseModel):
    identification: str
    password: str
    name: str
    insurance: str
