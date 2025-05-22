from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from app.invoice_detail.dto.invoice_detail_dto import InvoiceDetailDTO
class InvoiceDTO(BaseModel):
    customer_identification: str = Field(description="Primary customer identification")
    details: List[InvoiceDetailDTO] = Field(description="Invoice details")