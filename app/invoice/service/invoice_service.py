from datetime import datetime, timedelta
from typing import List
from uuid import UUID
import uuid

from fastapi.encoders import jsonable_encoder
from app.common import constants
from app.common.mapper import Mapper
from app.customer.repository.customer_repository import CustomerRepository
from app.exception.exception_handler import entity_not_found_exception
from app.invoice.dto.invoice_dto import InvoiceDTO
from app.invoice.repository.invoice_repository import InvoiceRepository
from app.product.entity.product import Product
from app.product.repository.product_repository import ProductRepository

class InvoiceService:

    def __init__(self, invoice_repository: InvoiceRepository, customer_repository: CustomerRepository, product_repository: ProductRepository):
        self.invoice_repository = invoice_repository
        self.customer_repository = customer_repository
        self.product_repository = product_repository
    
    def get(self):
        invoices =  self.invoice_repository.get()
        invoice_response_dto = [Mapper.invoice_to_invoice_response_dto(invoice) for invoice in invoices]
        return invoice_response_dto

    def get_by_id(self, id: UUID):
        invoice = self.invoice_repository.get_by_id(id)
        if not invoice:
            raise entity_not_found_exception(constants.invoice_not_found)
        invoice_response_dto = Mapper.invoice_to_invoice_response_dto(invoice)
        return invoice_response_dto
    
    def create(self, invoice_dto: InvoiceDTO):
        customer_exists = self.customer_repository.get_by_auth_identification(invoice_dto.customer_identification)
        if not customer_exists:
            raise entity_not_found_exception(constants.customer_not_found)
        total = 0
        products : List[Product] = []
        for detail in invoice_dto.details:
            product_exists = self.product_repository.get_by_id(detail.product.id)
            if not product_exists:
                raise entity_not_found_exception(constants.product_not_found)
            if product_exists.stock < detail.quantity:
                raise entity_not_found_exception(constants.stock_not_available)
            detail.subtotal_tax = ((product_exists.price * detail.quantity) * product_exists.tax)/100
            detail.subtotal = product_exists.price * detail.quantity
            product_exists.stock = product_exists.stock - detail.quantity
            total = total + detail.subtotal + detail.subtotal_tax
            products.append(product_exists)
        date = datetime.now()
        code = constants+"-"+str(uuid.uuid4())
        invoice = Mapper.invoice_dto_to_invoice(code, date, total, invoice_dto.details)
        invoice = self.invoice_repository.create(invoice)
        invoice_response_dto = Mapper.invoice_to_invoice_response_dto(invoice)
        return invoice_response_dto
    
    def update(self, id: UUID, invoice_dto: InvoiceDTO):
        invoice = self.invoice_repository.get_by_id(id)
        if not invoice:
            raise entity_not_found_exception(constants.invoice_not_found)
        invoice = Mapper.invoice_dto_to_invoice(invoice_dto)
        invoice = self.invoice_repository.update(invoice)
        return invoice

    def delete(self, id: UUID):
        invoice = self.invoice_repository.get_by_id(id)
        if not invoice:
            raise entity_not_found_exception(constants.invoice_not_found)
        self.invoice_repository.delete(invoice)