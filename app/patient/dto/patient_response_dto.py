from pydantic import BaseModel
from app.patient.entity.patient import Patient

class PatientResponseDTO(BaseModel):
    name: str
    insurance: str

def patient_to_dto(patient: Patient):
    return PatientResponseDTO(
        name = patient.name,
        insurance = patient.insurance
    )