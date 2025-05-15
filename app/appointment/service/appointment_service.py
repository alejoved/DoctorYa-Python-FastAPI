from datetime import timedelta
from uuid import UUID
from app.common import constants
from app.common.mapper import Mapper
from app.exception.exception_handler import entity_exists_exception, entity_not_exists_exception
from app.appointment.dto.appointment_dto import AppointmentDTO
from app.appointment.repository.appointment_repository import AppointmentRepository
from passlib.context import CryptContext

from app.patient.repository.patient_repository import PatientRepository
from app.physician.repository.physician_repository import PhysicianRepository

class AppointmentService:

    def __init__(self, appointment_repository: AppointmentRepository, patient_repository: PatientRepository, physician_repository: PhysicianRepository):
        self.appointment_repository = appointment_repository
        self.patient_repository = patient_repository
        self.physician_repository = physician_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get(self):
        return self.appointment_repository.get()

    def get_by_id(self, id: UUID):
        appointment = self.appointment_repository.get_by_id(id)
        if not appointment:
            raise entity_not_exists_exception(constants.appointment_not_found)
        appointment_response_dto = Mapper.appointment_to_appointment_response_dto(appointment)
        return appointment_response_dto
    
    def create(self, appointment_dto: AppointmentDTO):
        patient_exists = self.patient_repository.get_by_auth_identification(appointment_dto.patient_identification)
        if not patient_exists:
            raise entity_not_exists_exception(constants.patient_not_found)
        physician_exists = self.physician_repository.get_by_auth_identification(appointment_dto.physician_identification)
        if not physician_exists:
            raise entity_not_exists_exception(constants.physician_not_found)
        start_date = appointment_dto.start_date
        end_date = start_date + timedelta(minutes=appointment_dto.duration)
        appointment_exists = self.appointment_repository.find_overlapping(start_date, end_date, appointment_dto.physician_identification)
        if len(appointment_exists) > 0:
            raise entity_exists_exception(constants.appointment_exists)
        appointment = Mapper.appointment_dto_to_appointment(appointment_dto, end_date, patient_exists, physician_exists)
        appointment = self.appointment_repository.create(appointment)
        appointment_response_dto = Mapper.appointment_to_appointment_response_dto(appointment)
        return appointment_response_dto
    
    def update(self, id: UUID, patient_dto: AppointmentDTO):
        patient = self.appointment_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient = Mapper.patient_dto_to_patient(patient_dto)
        patient = self.appointment_repository.update(patient)
        return patient

    def delete(self, id: UUID):
        appointment = self.appointment_repository.get_by_id(id)
        if not appointment:
            raise entity_not_exists_exception(constants.patient_not_found)
        self.appointment_repository.delete(appointment)