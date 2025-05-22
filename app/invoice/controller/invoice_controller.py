from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.customer.repository.customer_repository import CustomerRepository
from app.invoice.dto.invoice_response_dto import InvoiceResponseDTO
from app.common.role import Role
from app.config.auth_config import valid_role
from app.invoice.dto.invoice_dto import InvoiceDTO
from app.invoice.repository.invoice_repository import InvoiceRepository
from app.invoice.service.invoice_service import InvoiceService
from app.product.repository.product_repository import ProductRepository

invoice_route = APIRouter()

def get_invoice_service():
    invoice_repository = InvoiceRepository()
    customer_repository = CustomerRepository()
    product_repository = ProductRepository()
    return InvoiceService(invoice_repository, customer_repository, product_repository)

@invoice_route.get("/api/invoice", response_model=List[InvoiceResponseDTO], response_model_exclude_none=True, tags=["Invoices"],
                       summary="Get all invoices currently",
                       responses={200: {"description": "Get all invoices successfully"}, 
                                  500: {"description": "Internal server error"}})
def get(invoice_service: InvoiceService = Depends(get_invoice_service)):
    invoice_response_dto = invoice_service.get()
    return invoice_response_dto

@invoice_route.get("/api/invoice/{id}", response_model=InvoiceResponseDTO, response_model_exclude_none=True, tags=["Invoices"],
                       summary="Get an invoice existing by uuid",
                       responses={200: {"description": "Get an invoice successfully"},
                                  404: {"description": "Invoice not found"}, 
                                  500: {"description": "Internal server error"}})
def get_by_id(id: UUID, invoice_service: InvoiceService = Depends(get_invoice_service)):
    invoice_response_dto = invoice_service.get_by_id(id)
    return invoice_response_dto

@invoice_route.post("/api/invoice", response_model=InvoiceResponseDTO, response_model_exclude_none=True, tags=["Invoices"],
                        summary="Create a new invoice associated with a patient and physician",
                       responses={200: {"description": "Invoice created successfully"},
                                  404: {"description": "Patient or physician not found"}, 
                                  500: {"description": "Internal server error"}})
def create(invoice_dto: InvoiceDTO, dep = Depends(valid_role(Role.ADMIN)), invoice_service: InvoiceService = Depends(get_invoice_service)):
    invoice_response_dto = invoice_service.create(invoice_dto)
    return invoice_response_dto

@invoice_route.put("/api/invoice/{id}", response_model=InvoiceResponseDTO, response_model_exclude_none=True, tags=["Invoices"],
                       summary="Update data about an invoice by uuid",
                       responses={200: {"description": "Invoice updated successfully"},
                                  404: {"description": "Invoice not found"}, 
                                  500: {"description": "Internal server error"}})
def update(id: UUID, invoice_dto: InvoiceDTO, invoice_service: InvoiceService = Depends(get_invoice_service)):
    invoice_response_dto = invoice_service.update(id, invoice_dto)
    return invoice_response_dto

@invoice_route.delete("/api/invoice/{id}", tags=["Invoices"],
                        summary="Delete an invoice by uuid",
                        responses={200: {"description": "Invoice deleted successfully"},
                                  404: {"description": "Invoice not found"}, 
                                  500: {"description": "Internal server error"}})
def delete(id: UUID, dep = Depends(valid_role(Role.ADMIN)), invoice_service: InvoiceService = Depends(get_invoice_service)):
    invoice_service.delete(id)