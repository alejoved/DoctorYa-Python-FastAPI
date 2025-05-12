from uuid import UUID

from sqlalchemy import and_, or_
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
from app.appointment.entity.appointment import Appointment
from app.physician.entity.physician import Physician

class AppointmentRepository:
    def get(self):
        db = SessionLocal()
        appointments = db.query(Appointment).all()
        return appointments
    
    def get_by_id(self, id: UUID):
        db = SessionLocal()
        appointment = db.query(Appointment).filter(Appointment.id == id).first()
        return appointment
    
    def find_overlapping(self, start_date, end_date, physician_identification: str):
        db = SessionLocal()
        appointments = db.query(Appointment).join(Appointment.physician).join(Physician.auth).filter(
        Appointment.start_date < end_date,
        Appointment.end_date > start_date,
        Auth.identification == physician_identification
        ).all()
        return appointments
    
    def create(self, appointment: Appointment):
        db = SessionLocal()
        db.add(appointment)
        db.commit()
        db.refresh(appointment)
        return appointment
    
    def update(self, appointment: Appointment):
        db = SessionLocal()
        db.commit()
        db.refresh(appointment)
        return appointment

    def delete(self, appointment: Appointment):
        db = SessionLocal()
        db.delete(appointment)
        db.commit()