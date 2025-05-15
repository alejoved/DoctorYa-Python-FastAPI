from pydantic import BaseModel, Field
from app.patient.entity.patient import Patient

class PatientDTO(BaseModel):
    identification: str = Field(description = "Primary identification for the patient")
    password: str = Field(description = "Password for the login")
    name: str = Field(description = "Patient full name")
    insurance: str = Field(description = "Name of the health insurance")
