from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, field_serializer

from app.invoice_detail.dto.invoice_detail_response_dto import InvoiceDetailResponseDTO

class InvoiceResponseDTO(BaseModel):
    id: Optional[str] = Field(default = None, description="Invoice ID")
    code: Optional[str] = Field(default = None, description="Invoice full code")
    date: Optional[datetime] = Field(default = None, description="Invoice register date", example = "2025-05-10 14:00:00")
    total: Optional[float] = Field(default = None, description="Invoice total")
    details: Optional[List[InvoiceDetailResponseDTO]] = Field(default = None, description="Main data details")

    @field_serializer('date')
    def serialize_datetime(self, value: datetime, _info):
        return value.strftime('%Y-%m-%d %H:%M:%S')