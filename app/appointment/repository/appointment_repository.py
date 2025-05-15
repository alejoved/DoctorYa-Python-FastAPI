from contextlib import contextmanager
from uuid import UUID
from sqlalchemy.orm import joinedload
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
from app.appointment.entity.appointment import Appointment
from app.patient.entity.patient import Patient
from app.physician.entity.physician import Physician

@contextmanager
def get_session():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

class AppointmentRepository:
    def get(self):
        with get_session() as db:
            return db.query(Appointment).all()
    
    def get_by_id(self, id: UUID):
        with get_session() as db:
            return db.query(Appointment).filter(Appointment.id == id).first()
    
    def find_overlapping(self, start_date, end_date, physician_identification: str):
        with get_session() as db:
            return db.query(Appointment).join(Appointment.physician).join(Physician.auth).filter(
            Appointment.start_date < end_date,
            Appointment.end_date > start_date,
            Auth.identification == physician_identification
            ).all()
    
    def create(self, appointment: Appointment):
        with get_session() as db:
            db.add(appointment)
            db.flush()
            appointment_with_relations = db.query(Appointment).options(
            joinedload(Appointment.patient).joinedload(Patient.auth),
            joinedload(Appointment.physician).joinedload(Physician.auth)
            ).filter(Appointment.id == appointment.id).first()
            return appointment_with_relations
    
    def update(self, appointment: Appointment):
        with get_session() as db:
            db.merge(appointment)
            db.flush()
            db.refresh(appointment)
            return appointment

    def delete(self, appointment: Appointment):
        with get_session() as db:
            db.delete(appointment)