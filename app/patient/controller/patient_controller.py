from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi_jwt import JwtAuthorizationCredentials
from app.auth.repository.auth_repository import AuthRepository
from app.common.role import Role
from app.config.auth_config import access_security, valid_role
from app.patient.dto.patient_dto import PatientDTO
from app.patient.repository.patient_repository import PatientRepository
from app.patient.service.patient_service import PatientService

patient_route = APIRouter()

def get_patient_service():
    patient_repository = PatientRepository()
    auth_repository = AuthRepository()
    return PatientService(patient_repository, auth_repository)

@patient_route.get("/api/patient")
def get(patient_service: PatientService = Depends(get_patient_service)):
    patient_response_dto = patient_service.get()
    return patient_response_dto

@patient_route.get("/api/patient/{id}")
def get_by_id(id: UUID, patient_service: PatientService = Depends(get_patient_service)):
    patient_response_dto = patient_service.get_by_id(id)
    return patient_response_dto

@patient_route.post("/api/patient")
def create(patient_dto: PatientDTO, dep = Depends(valid_role(Role.ADMIN)), patient_service: PatientService = Depends(get_patient_service)):
    patient_response_dto = patient_service.create(patient_dto)
    return patient_response_dto

@patient_route.put("/api/patient/{id}")
def update(id: UUID, patient_dto: PatientDTO, patient_service: PatientService = Depends(get_patient_service)):
    patient_response_dto = patient_service.update(id, patient_dto)
    return patient_response_dto

@patient_route.delete("/api/patient/{id}")
def delete(id: UUID, dep = Depends(valid_role(Role.ADMIN)), patient_service: PatientService = Depends(get_patient_service)):
    patient_service.delete(id)