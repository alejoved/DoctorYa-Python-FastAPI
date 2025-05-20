from datetime import timedelta
from uuid import UUID
from app.common import constants
from app.common.mapper import Mapper
from app.exception.exception_handler import entity_exists_exception, entity_not_exists_exception
from app.invoice.dto.invoice_dto import InvoiceDTO
from app.invoice.repository.invoice_repository import InvoiceRepository
from passlib.context import CryptContext

from app.patient.repository.patient_repository import PatientRepository
from app.physician.repository.physician_repository import PhysicianRepository

class InvoiceService:

    def __init__(self, invoice_repository: InvoiceRepository, patient_repository: PatientRepository, physician_repository: PhysicianRepository):
        self.invoice_repository = invoice_repository
        self.patient_repository = patient_repository
        self.physician_repository = physician_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get(self):
        return self.invoice_repository.get()

    def get_by_id(self, id: UUID):
        invoice = self.invoice_repository.get_by_id(id)
        if not invoice:
            raise entity_not_exists_exception(constants.invoice_not_found)
        invoice_response_dto = Mapper.invoice_to_invoice_response_dto(invoice)
        return invoice_response_dto
    
    def create(self, invoice_dto: InvoiceDTO):
        patient_exists = self.patient_repository.get_by_auth_identification(invoice_dto.patient_identification)
        if not patient_exists:
            raise entity_not_exists_exception(constants.patient_not_found)
        physician_exists = self.physician_repository.get_by_auth_identification(invoice_dto.physician_identification)
        if not physician_exists:
            raise entity_not_exists_exception(constants.physician_not_found)
        start_date = invoice_dto.start_date
        end_date = start_date + timedelta(minutes=invoice_dto.duration)
        invoice_exists = self.invoice_repository.find_overlapping(start_date, end_date, invoice_dto.physician_identification)
        if len(invoice_exists) > 0:
            raise entity_exists_exception(constants.invoice_exists)
        invoice = Mapper.invoice_dto_to_invoice(invoice_dto, end_date, patient_exists, physician_exists)
        invoice = self.invoice_repository.create(invoice)
        invoice_response_dto = Mapper.invoice_to_invoice_response_dto(invoice)
        return invoice_response_dto
    
    def update(self, id: UUID, patient_dto: InvoiceDTO):
        patient = self.invoice_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient = Mapper.patient_dto_to_patient(patient_dto)
        patient = self.invoice_repository.update(patient)
        return patient

    def delete(self, id: UUID):
        invoice = self.invoice_repository.get_by_id(id)
        if not invoice:
            raise entity_not_exists_exception(constants.patient_not_found)
        self.invoice_repository.delete(invoice)