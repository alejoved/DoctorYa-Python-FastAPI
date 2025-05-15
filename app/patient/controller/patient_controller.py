from uuid import UUID
from fastapi import APIRouter, Depends
from app.auth.repository.auth_repository import AuthRepository
from app.common.role import Role
from app.config.auth_config import valid_role
from app.patient.dto.patient_dto import PatientDTO
from app.patient.dto.patient_response_dto import PatientResponseDTO
from app.patient.repository.patient_repository import PatientRepository
from app.patient.service.patient_service import PatientService

patient_route = APIRouter()

def get_patient_service():
    patient_repository = PatientRepository()
    auth_repository = AuthRepository()
    return PatientService(patient_repository, auth_repository)

@patient_route.get("/api/patient", response_model=PatientResponseDTO, response_model_exclude_none=True, tags=["Patient"],
                   summary="Get all patients currently",
                       responses={200: {"description": "Get all patients successfully"},
                                  500: {"description": "Internal server error"}})
def get(patient_service: PatientService = Depends(get_patient_service)):
    patient_response_dto = patient_service.get()
    return patient_response_dto

@patient_route.get("/api/patient/{id}", response_model=PatientResponseDTO, response_model_exclude_none=True, tags=["Patient"],
                    summary="Get an patient existing by uuid",
                    responses={200: {"description": "Get an patient successfully"},
                                404: {"description": "Patient not found"}, 
                                500: {"description": "Internal server error"}})
def get_by_id(id: UUID, patient_service: PatientService = Depends(get_patient_service)):
    patient_response_dto = patient_service.get_by_id(id)
    return patient_response_dto

@patient_route.post("/api/patient", response_model=PatientResponseDTO, response_model_exclude_none=True, tags=["Patient"],
                    summary="Create a new patient associated with a identification, name and an medical code",
                    responses={200: {"description": "Patient created successfully"},
                                409: {"description": "Patient already exists"}, 
                                500: {"description": "Internal server error"}})
def create(patient_dto: PatientDTO, dep = Depends(valid_role(Role.ADMIN)), patient_service: PatientService = Depends(get_patient_service)):
    patient_response_dto = patient_service.create(patient_dto)
    return patient_response_dto

@patient_route.put("/api/patient/{id}", response_model=PatientResponseDTO, response_model_exclude_none=True, tags=["Patient"],
                    summary="Update data about a patient by uuid",
                    responses={200: {"description": "Patient updated successfully"},
                                404: {"description": "Patient not found"}, 
                                500: {"description": "Internal server error"}})
def update(id: UUID, patient_dto: PatientDTO, patient_service: PatientService = Depends(get_patient_service)):
    patient_response_dto = patient_service.update(id, patient_dto)
    return patient_response_dto

@patient_route.delete("/api/patient/{id}", tags=["Patient"],
                    summary="Delete an patient by uuid",
                    responses={200: {"description": "Patient deleted successfully"},
                                404: {"description": "Patient not found"}, 
                                500: {"description": "Internal server error"}})
def delete(id: UUID, dep = Depends(valid_role(Role.ADMIN)), patient_service: PatientService = Depends(get_patient_service)):
    patient_service.delete(id)