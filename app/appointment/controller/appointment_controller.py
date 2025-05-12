from uuid import UUID
from fastapi import APIRouter, Depends
from app.common.role import Role
from app.config.auth_config import valid_role
from app.appointment.dto.appointment_dto import AppointmentDTO
from app.appointment.repository.appointment_repository import AppointmentRepository
from app.appointment.service.appointment_service import AppointmentService
from app.patient.repository.patient_repository import PatientRepository
from app.physician.repository.physician_repository import PhysicianRepository

appointment_route = APIRouter()

def get_appointment_service():
    appointment_repository = AppointmentRepository()
    patient_repository = PatientRepository()
    physician_repository = PhysicianRepository()
    return AppointmentService(appointment_repository, patient_repository, physician_repository)

@appointment_route.get("/api/appointment")
def get(appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_response_dto = appointment_service.get()
    return appointment_response_dto

@appointment_route.get("/api/appointment/{id}")
def get_by_id(id: UUID, appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_response_dto = appointment_service.get_by_id(id)
    return appointment_response_dto

@appointment_route.post("/api/appointment")
def create(appointment_dto: AppointmentDTO, dep = Depends(valid_role(Role.ADMIN)), appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_response_dto = appointment_service.create(appointment_dto)
    return appointment_response_dto

@appointment_route.put("/api/appointment/{id}")
def update(id: UUID, appointment_dto: AppointmentDTO, appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_response_dto = appointment_service.update(id, appointment_dto)
    return appointment_response_dto

@appointment_route.delete("/api/appointment/{id}")
def delete(id: UUID, dep = Depends(valid_role(Role.ADMIN)), appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_service.delete(id)