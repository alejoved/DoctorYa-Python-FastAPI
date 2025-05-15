from typing import Optional
from pydantic import BaseModel, Field
from app.auth.dto.auth_response_dto import AuthResponseDTO
from app.patient.entity.patient import Patient

class PatientResponseDTO(BaseModel):
    name: Optional[str] = Field(default = None, description = "Patient full name")
    insurance: Optional[str] = Field(default = None, description = "Name of the heatlh insurance")
    auth: Optional[AuthResponseDTO] = Field(default = None, description = "Authentication data of the patient")