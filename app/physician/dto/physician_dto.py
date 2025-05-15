from pydantic import BaseModel, Field
from app.physician.entity.physician import Physician

class PhysicianDTO(BaseModel):
    identification: str = Field(description = "Primary identification for the physician")
    password: str = Field(description = "Password for the log in")
    name: str = Field(description = "Physician full name")
    code: str = Field(description = "General medical code")
    speciality: str = Field(description = "Speciality field of the physician")


