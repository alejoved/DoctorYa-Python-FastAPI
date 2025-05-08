from pydantic import BaseModel
from app.patient.entity.patient import Patient

class PatientResponseDTO(BaseModel):
    name: str
    insurance: str