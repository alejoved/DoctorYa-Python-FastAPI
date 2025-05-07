from fastapi import Depends
from app.common import constants
from app.exception.exception_handler import entity_not_exists_exception
from app.patient.dto.patient_dto import PatientDTO, dto_to_patient
from app.patient.dto.patient_response_dto import patient_to_dto
from app.patient.repository.patient_repository import PatientRepository

class PatientService:
    def get_patient_repository():
        return PatientRepository()
    
    def get(patient_repository: PatientRepository = Depends(get_patient_repository)):
        return patient_repository.get()

    def get_by_id(id: str, patient_repository: PatientRepository = Depends(get_patient_repository)):
        patient = patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient_response_dto = patient_to_dto(patient)
        return patient_response_dto
    
    def create(patient_dto: PatientDTO, patient_repository: PatientRepository = Depends(get_patient_repository)):
        patient = dto_to_patient(patient_dto)
        patient = patient_repository.create(patient)
        patient_response_dto = patient_to_dto(patient)
        return patient_response_dto
    
    def update(id: str, patient_dto: PatientDTO, patient_repository: PatientRepository = Depends(get_patient_repository)):
        patient = patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient = dto_to_patient(patient_dto)
        patient = patient_repository.update(patient)
        return patient

    def delete(id: str, patient_repository: PatientRepository = Depends(get_patient_repository)):
        patient = patient_repository.get_by_id(id)
        if not patient:
            raise entity_not_exists_exception(constants.patient_not_found)
        patient_repository.delete(patient)

