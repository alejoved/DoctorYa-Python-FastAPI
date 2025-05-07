from pydantic import BaseModel
from app.patient.entity.patient import Patient

class PatientDTO(BaseModel):
    identification: str
    password: str
    name: str
    insurance: str

def dto_to_patient(patient_dto: PatientDTO):
    return Patient(
        name = patient_dto.name,
        insurance = patient_dto.insurance
    )
