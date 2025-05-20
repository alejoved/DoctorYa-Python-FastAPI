from datetime import datetime
from pydantic import BaseModel, Field, field_serializer
class InvoiceDTO(BaseModel):
    start_date: datetime = Field(description="Initial date of the invoice", example="2025-05-10 14:00:00")
    duration: int = Field(description="Invoice duration in minutes")
    reason: str = Field(description="Description about the invoice")
    patient_identification: str = Field(description="Primary identification of the patient")
    physician_identification: str = Field(description="Primary identification of the physician")

    @field_serializer('start_date')
    def serialize_datetime(self, value: datetime, _info):
        return value.strftime('%Y-%m-%d %H:%M:%S')