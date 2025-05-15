from uuid import UUID
from app.auth.entity.auth import Auth
from app.auth.repository.auth_repository import AuthRepository
from app.common import constants
from app.common.mapper import Mapper
from app.common.role import Role
from app.exception.exception_handler import entity_exists_exception, entity_not_exists_exception
from app.patient.dto.patient_dto import PatientDTO
from app.patient.repository.patient_repository import PatientRepository
from passlib.context import CryptContext

class PatientService:

    def __init__(self, patient_repository: PatientRepository, auth_repository: AuthRepository):
        self.patient_repository = patient_repository
        self.auth_repository = auth_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get(self):
        patients = self.patient_repository.get()
        patient_response_dto = [Mapper.patient_to_patient_response_dto(patient) for patient in patients]
        return patient_response_dto

    def get_by_id(self, id: UUID):
        patient = self.patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient_response_dto = Mapper.patient_to_patient_response_dto(patient)
        return patient_response_dto
    
    def get_by_identification(self, identification: str):
        patient = self.patient_repository.get_by_auth_identification(identification)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient_response_dto = Mapper.patient_to_patient_response_dto(patient)
        return patient_response_dto
    
    def create(self, patient_dto: PatientDTO):
        authExists = self.auth_repository.get_by_identification(patient_dto.identification)
        if authExists:
            raise entity_exists_exception(constants.auth_exists)
        auth = Auth()
        auth.identification = patient_dto.identification
        auth.password = self.pwd_context.hash(patient_dto.password)
        auth.role = Role.PATIENT
        patient = Mapper.patient_dto_to_patient(patient_dto)
        patient.auth = auth
        patient = self.patient_repository.create(patient)
        patient_response_dto = Mapper.patient_to_patient_response_dto(patient)
        return patient_response_dto
    
    def update(self, id: UUID, patient_dto: PatientDTO):
        patient = self.patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient = Mapper.patient_dto_to_patient(patient_dto)
        patient = self.patient_repository.update(patient)
        return patient

    def delete(self, id: UUID):
        patient = self.patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        self.patient_repository.delete(patient)

