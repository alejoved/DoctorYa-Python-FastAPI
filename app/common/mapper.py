from datetime import datetime
from app.appointment.dto.appointment_dto import AppointmentDTO
from app.appointment.dto.appointment_response_dto import AppointmentResponseDTO
from app.appointment.entity.appointment import Appointment
from app.auth.dto.auth_response_dto import AuthResponseDTO
from app.auth.dto.login_response_dto import LoginResponseDTO
from app.auth.dto.register_response_dto import RegisterResponseDTO
from app.auth.entity.auth import Auth
from app.common.role import Role
from app.patient.dto.patient_dto import PatientDTO
from app.patient.dto.patient_response_dto import PatientResponseDTO
from app.patient.entity.patient import Patient
from app.physician.dto.physician_dto import PhysicianDTO
from app.physician.dto.physician_response_dto import PhysicianResponseDTO
from app.physician.entity.physician import Physician

class Mapper:
    @staticmethod
    def patient_dto_to_patient(patient_dto: PatientDTO):
        return Patient(
            name = patient_dto.name,
            insurance = patient_dto.insurance
    )
    @staticmethod
    def patient_to_patient_response_dto(patient: Patient) -> PatientResponseDTO:
        return PatientResponseDTO(
            name = patient.name,
            insurance = patient.insurance,
            auth = AuthResponseDTO(identification = patient.auth.identification)
        )
    @staticmethod
    def physician_dto_to_physician(physician_dto: PhysicianDTO) -> Physician:
        return Physician(
            name = physician_dto.name,
            code = physician_dto.code,
            speciality = physician_dto.speciality
        )
    @staticmethod
    def physician_to_physician_response_dto(physician: Physician) -> PhysicianResponseDTO:
        return PhysicianResponseDTO(
            name = physician.name,
            code = physician.code,
            speciality = physician.speciality,
            auth = AuthResponseDTO(identification = physician.auth.identification)
        )
    @staticmethod
    def login_to_login_response_dto(token: str, role: Role) -> LoginResponseDTO:
        return LoginResponseDTO (
            token = token,
            role = role
        )
    @staticmethod
    def auth_to_register_response_dto(auth: Auth) -> RegisterResponseDTO:
        return RegisterResponseDTO (
            identification = auth.identification
        )
    
    @staticmethod
    def appointment_dto_to_appointment(appointment_dto: AppointmentDTO, end_date: datetime, patient: Patient, physician: Physician) -> Appointment:
        return Appointment (
            reason = appointment_dto.reason,
            start_date = appointment_dto.start_date,
            end_date = end_date,
            patient = patient,
            physician = physician
        )
    
    @staticmethod
    def appointment_to_appointment_response_dto(appointment: Appointment) -> AppointmentResponseDTO:
        return AppointmentResponseDTO (
            start_date = appointment.start_date,
            end_date = appointment.end_date,
            reason = appointment.reason,
            patient = appointment.patient,
            physician = appointment.physician
        )