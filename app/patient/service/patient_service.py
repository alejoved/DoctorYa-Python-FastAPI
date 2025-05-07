
from uuid import UUID
from app.common import constants
from app.exception.exception_handler import entity_not_exists_exception
from app.patient.dto.patient_dto import PatientDTO, dto_to_patient
from app.patient.dto.patient_response_dto import patient_to_dto
from app.patient.repository.patient_repository import PatientRepository

class PatientService:

    def __init__(self, patient_repository: PatientRepository):
        self.patient_repository = patient_repository
    
    def get(self):
        return self.patient_repository.get()

    def get_by_id(self, id: UUID):
        patient = self.patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient_response_dto = patient_to_dto(patient)
        return patient_response_dto
    
    def create(self, patient_dto: PatientDTO):
        patient = dto_to_patient(patient_dto)
        patient = self.patient_repository.create(patient)
        print(patient.name)
        patient_response_dto = patient_to_dto(patient)
        return patient_response_dto
    
    def update(self, id: UUID, patient_dto: PatientDTO):
        patient = self.patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient = dto_to_patient(patient_dto)
        patient = self.patient_repository.update(patient)
        return patient

    def delete(self, id: UUID):
        patient = self.patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        self.patient_repository.delete(patient)

