from contextlib import contextmanager
from uuid import UUID
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
from app.patient.entity.patient import Patient
from sqlalchemy.orm import joinedload

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

class PatientRepository:
    def get(self):
        with get_session() as db:
            return db.query(Patient).options(
            joinedload(Patient.auth)).all()
    
    def get_by_id(self, id: UUID):
        with get_session() as db:
            return db.query(Patient).filter(Patient.id == id).first()
    
    def get_by_auth_identification(self, identification: str):
        with get_session() as db:
            return db.query(Patient).join(Patient.auth).filter(Auth.identification == identification).first()
    
    def create(self, patient: Patient):
        with get_session() as db:
            db.add(patient)
            db.flush() 
            db.refresh(patient)
            return patient
    
    def update(self, patient: Patient):
        with get_session() as db:
            db.merge(patient)
            db.flush()
            db.refresh(patient)
            return patient

    def delete(self, patient: Patient):
        with get_session() as db:
            db.delete(patient)


