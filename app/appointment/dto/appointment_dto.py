from datetime import datetime
from pydantic import BaseModel, field_serializer
class AppointmentDTO(BaseModel):
    start_date: datetime
    duration: int
    reason: str
    patient_identification: str
    physician_identification: str

    @field_serializer('start_date')
    def serialize_datetime(self, value: datetime, _info):
        return value.strftime('%Y-%m-%d %H:%M:%S')