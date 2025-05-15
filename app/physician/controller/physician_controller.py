from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.auth.repository.auth_repository import AuthRepository
from app.physician.dto.physician_dto import PhysicianDTO
from app.physician.dto.physician_response_dto import PhysicianResponseDTO
from app.physician.repository.physician_repository import PhysicianRepository
from app.physician.service.physician_service import PhysicianService

physician_route = APIRouter()

def get_physician_service():
    physician_repository = PhysicianRepository()
    auth_repository = AuthRepository()
    return PhysicianService(physician_repository, auth_repository)

@physician_route.get("/api/physician", response_model=List[PhysicianResponseDTO], response_model_exclude_none=True, tags=["Physician"],
                    summary="Get all physicians currently",
                    responses={200: {"description": "Get all the physicians Successfully"},
                                500: {"description": "Internal server error"}})
def get(physician_service: PhysicianService = Depends(get_physician_service)):
    physician_response_dto = physician_service.get()
    return physician_response_dto

@physician_route.get("/api/physician/{id}", response_model=PhysicianResponseDTO, response_model_exclude_none=True, tags=["Physician"],
                    summary="Get an physician existing by uuid",
                    responses={200: {"description": "Get an physician successfully"},
                                404: {"description": "Physician not found"}, 
                                500: {"description": "Internal server error"}})
def get_by_id(id: UUID, physician_service: PhysicianService = Depends(get_physician_service)):
    physician_response_dto = physician_service.get_by_id(id)
    return physician_response_dto

@physician_route.post("/api/physician", response_model=PhysicianResponseDTO, response_model_exclude_none=True, tags=["Physician"],
                    summary="Create a new physician associated with a name and medical code",
                    responses={200: {"description": "Physician created successfully"},
                                404: {"description": "Physician not found"}, 
                                500: {"description": "Internal server error"}})
def create(physician_dto: PhysicianDTO, physician_service: PhysicianService = Depends(get_physician_service)):
    physician_response_dto = physician_service.create(physician_dto)
    return physician_response_dto

@physician_route.put("/api/physician/{id}", response_model=PhysicianResponseDTO, response_model_exclude_none=True, tags=["Physician"],
                    summary="Update data about a physician by uuid",
                    responses={200: {"description": "Physician updated successfully"},
                                404: {"description": "Physician not found"}, 
                                500: {"description": "Internal server error"}})
def update(id: UUID, physician_dto: PhysicianDTO, physician_service: PhysicianService = Depends(get_physician_service)):
    physician_response_dto = physician_service.update(id, physician_dto)
    return physician_response_dto

@physician_route.delete("/api/physician/{id}", tags=["Physician"],
                    summary="",
                    responses={200: {"description": "Physician updated successfully"},
                                404: {"description": "Physician not found"}, 
                                500: {"description": "Internal server error"}})
def delete(id: UUID, physician_service: PhysicianService = Depends(get_physician_service)):
    physician_service.delete(id)