from datetime import datetime
from pydantic import BaseModel, field_serializer
from app.patient.dto.patient_response_dto import PatientResponseDTO
from app.physician.dto.physician_response_dto import PhysicianResponseDTO

class AppointmentResponseDTO(BaseModel):
    start_date: datetime
    end_date: datetime
    reason: str
    patient: PatientResponseDTO
    physician: PhysicianResponseDTO

    @field_serializer('start_date', 'end_date')
    def serialize_datetime(self, value: datetime, _info):
        return value.strftime('%Y-%m-%d %H:%M:%S')