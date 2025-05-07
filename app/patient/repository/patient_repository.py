from app.common import constants
from app.common.datasource import SessionLocal
from app.exception.exception_handler import entity_not_exists_exception
from app.patient.entity.patient import Patient

class PatientRepository:
    def get():
        db = SessionLocal()
        patients = db.query(Patient).all()
        return patients
    
    def get_by_id(id: str):
        db = SessionLocal()
        patient = db.query(Patient).filter(Patient.id == id).first()
        return patient
    
    def create(patient: Patient):
        db = SessionLocal()
        db.add(patient)
        db.commit()
        db.refresh(patient)
        return patient
    
    def update(patient: Patient):
        db = SessionLocal()
        db.commit()
        db.refresh(patient)

    def delete(patient: Patient):
        db = SessionLocal()
        db.delete(patient)
        db.commit()


