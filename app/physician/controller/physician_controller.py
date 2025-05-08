from uuid import UUID
from fastapi import APIRouter, Depends

from app.auth.repository.auth_repository import AuthRepository
from app.physician.dto.physician_dto import PhysicianDTO
from app.physician.repository.physician_repository import PhysicianRepository
from app.physician.service.physician_service import PhysicianService

physician_route = APIRouter()

def get_physician_service():
    physician_repository = PhysicianRepository()
    auth_repository = AuthRepository()
    return PhysicianService(physician_repository, auth_repository)

@physician_route.get("/api/physician")
def get(physician_service: PhysicianService = Depends(get_physician_service)):
    physician_response_dto = physician_service.get()
    return physician_response_dto

@physician_route.get("/api/physician/{id}")
def get_by_id(id: UUID, physician_service: PhysicianService = Depends(get_physician_service)):
    physician_response_dto = physician_service.get_by_id(id)
    return physician_response_dto

@physician_route.post("/api/physician")
def create(physician_dto: PhysicianDTO, physician_service: PhysicianService = Depends(get_physician_service)):
    physician_response_dto = physician_service.create(physician_dto)
    return physician_response_dto

@physician_route.put("/api/physician/{id}")
def update(id: UUID, physician_dto: PhysicianDTO, physician_service: PhysicianService = Depends(get_physician_service)):
    physician_response_dto = physician_service.update(id, physician_dto)
    return physician_response_dto

@physician_route.delete("/api/physician/{id}")
def delete(id: UUID, physician_service: PhysicianService = Depends(get_physician_service)):
    physician_service.delete(id)