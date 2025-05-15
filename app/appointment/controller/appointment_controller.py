from uuid import UUID
from fastapi import APIRouter, Depends
from app.appointment.dto.appointment_response_dto import AppointmentResponseDTO
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

@appointment_route.get("/api/appointment", response_model=AppointmentResponseDTO, response_model_exclude_none=True, tags=["Appointments"],
                       summary="Get all appointments currently",
                       responses={200: {"description": "Get all appointments successfully"}, 
                                  500: {"description": "Internal server error"}})
def get(appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_response_dto = appointment_service.get()
    return appointment_response_dto

@appointment_route.get("/api/appointment/{id}", response_model=AppointmentResponseDTO, response_model_exclude_none=True, tags=["Appointments"],
                       summary="Get an appointment existing by uuid",
                       responses={200: {"description": "Get an appointment successfully"},
                                  404: {"description": "Appointment not found"}, 
                                  500: {"description": "Internal server error"}})
def get_by_id(id: UUID, appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_response_dto = appointment_service.get_by_id(id)
    return appointment_response_dto

@appointment_route.post("/api/appointment", response_model=AppointmentResponseDTO, response_model_exclude_none=True, tags=["Appointments"],
                        summary="Create a new appointment associated with a patient and physician",
                       responses={200: {"description": "Appointment created successfully"},
                                  404: {"description": "Patient or physician not found"}, 
                                  500: {"description": "Internal server error"}})
def create(appointment_dto: AppointmentDTO, dep = Depends(valid_role(Role.ADMIN)), appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_response_dto = appointment_service.create(appointment_dto)
    return appointment_response_dto

@appointment_route.put("/api/appointment/{id}", response_model=AppointmentResponseDTO, response_model_exclude_none=True, tags=["Appointments"],
                       summary="Update data about an appointment by uuid",
                       responses={200: {"description": "Appointment updated successfully"},
                                  404: {"description": "Appointment not found"}, 
                                  500: {"description": "Internal server error"}})
def update(id: UUID, appointment_dto: AppointmentDTO, appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_response_dto = appointment_service.update(id, appointment_dto)
    return appointment_response_dto

@appointment_route.delete("/api/appointment/{id}", tags=["Appointments"],
                        summary="Delete an appointment by uuid",
                        responses={200: {"description": "Appointment deleted successfully"},
                                  404: {"description": "Appointment not found"}, 
                                  500: {"description": "Internal server error"}})
def delete(id: UUID, dep = Depends(valid_role(Role.ADMIN)), appointment_service: AppointmentService = Depends(get_appointment_service)):
    appointment_service.delete(id)