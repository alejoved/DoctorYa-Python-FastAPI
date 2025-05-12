from pydantic import BaseModel
from app.auth.dto.auth_response_dto import AuthResponseDTO
from app.patient.entity.patient import Patient

class PatientResponseDTO(BaseModel):
    name: str
    insurance: str
    auth: AuthResponseDTO