from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_serializer
from app.patient.dto.patient_response_dto import PatientResponseDTO
from app.physician.dto.physician_response_dto import PhysicianResponseDTO

class AppointmentResponseDTO(BaseModel):
    id: Optional[str] = Field(default = None, description="Appointment ID")
    start_date: Optional[datetime] = Field(default = None, description="Date for to start medical appointment", example = "2025-05-10 14:00:00")
    end_date: Optional[datetime] = Field(default = None, description="Date for to end medical appointment", example = "2025-05-10 14:20:00")
    reason: Optional[str] = Field(default = None, description="Description about the appointment")
    patient: Optional[PatientResponseDTO] = Field(default = None, description="Main data about the patient")
    physician: Optional[PhysicianResponseDTO] = Field(default = None, description="Main data about the physician")

    @field_serializer('start_date', 'end_date')
    def serialize_datetime(self, value: datetime, _info):
        return value.strftime('%Y-%m-%d %H:%M:%S')