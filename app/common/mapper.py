from datetime import datetime
from typing import List
from uuid import UUID
from app.auth.dto.auth_response_dto import AuthResponseDTO
from app.auth.dto.login_response_dto import LoginResponseDTO
from app.auth.dto.register_response_dto import RegisterResponseDTO
from app.auth.entity.auth import Auth
from app.common.role import Role
from app.customer.dto.customer_dto import CustomerDTO
from app.customer.dto.customer_response_dto import CustomerResponseDTO
from app.customer.entity.customer import Customer
from app.invoice.dto.invoice_dto import InvoiceDTO
from app.invoice.dto.invoice_response_dto import InvoiceResponseDTO
from app.invoice.entity.invoice import Invoice
from app.invoice_detail.dto.invoice_detail_dto import InvoiceDetailDTO
from app.invoice_detail.dto.invoice_detail_response_dto import InvoiceDetailResponseDTO
from app.invoice_detail.entity.invoice_detail import InvoiceDetail
from app.product.dto.product_dto import ProductDTO
from app.product.dto.product_response_dto import ProductResponseDTO
from app.product.entity.product import Product

class Mapper:
    
    @staticmethod
    def login_to_login_response_dto(token: str, role: Role) -> LoginResponseDTO:
        return LoginResponseDTO (
            token = token,
            role = role
        )
    
    @staticmethod
    def auth_to_register_response_dto(auth: Auth) -> RegisterResponseDTO:
        return RegisterResponseDTO (
            identification = auth.identification
        )
    
    @staticmethod
    def customer_dto_to_customer(customer_dto: CustomerDTO):
        return Customer(
            name = customer_dto.name,
            address = customer_dto.address,
            auth = Auth(identification = customer_dto.identification, password = customer_dto.password)
    )
    @staticmethod
    def customer_to_customer_response_dto(customer: Customer) -> CustomerResponseDTO:
        return CustomerResponseDTO(
            name = customer.name,
            addres = customer.address,
            auth = AuthResponseDTO(identification = customer.auth.identification)
        )
    @staticmethod
    def product_dto_to_product(product_dto: ProductDTO) -> Product:
        return Product(
            name = product_dto.name,
            description = product_dto.description,
            price = product_dto.price,
            tax = product_dto.tax,
            stock = product_dto.stock
        )
    @staticmethod
    def product_to_product_response_dto(product: Product) -> ProductResponseDTO:
        return ProductResponseDTO(
            id = product.id,
            name = product.name,
            price = product.price,
            tax = product.tax,
            stock = product.stock
        )
    
    @staticmethod
    def invoice_dto_to_invoice(code: str, date: datetime, total: float, invoice_detail_dto: List[InvoiceDetailDTO]) -> Invoice:
        details : List[InvoiceDetail] = []
        for detail in invoice_detail_dto:
            invoice_detail = InvoiceDetail(quantity = detail.quantity, subtotal_tax = detail.subtotal_tax, subtotal = detail.subtotal, product_id = detail.product.id)
            details.append(invoice_detail)
        return Invoice (
            code = code,
            date = date,
            total = total,
            details = details
        )
    
    @staticmethod
    def invoice_to_invoice_response_dto(invoice: Invoice) -> InvoiceResponseDTO:
        details : List[InvoiceDetailResponseDTO] = []
        for invoice_detail in invoice.details:
            detail = InvoiceDetailResponseDTO(quantity=invoice_detail.quantity, subtotal_tax=invoice_detail.subtotal_tax, subtotal=invoice_detail.subtotal,
                                              product=ProductResponseDTO(name=invoice_detail.product.name))
            details.append(detail)
        return InvoiceResponseDTO (
            code = invoice.code,
            date = invoice.date,
            total = invoice.total,
            details = details,
        )