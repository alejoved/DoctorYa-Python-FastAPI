from uuid import UUID
from app.common.datasource import SessionLocal
from app.patient.entity.patient import Patient

class PatientRepository:
    def get(self):
        db = SessionLocal()
        patients = db.query(Patient).all()
        return patients
    
    def get_by_id(self, id: UUID):
        db = SessionLocal()
        patient = db.query(Patient).filter(Patient.id == id).first()
        return patient
    
    def create(self, patient: Patient):
        db = SessionLocal()
        db.add(patient)
        db.commit()
        db.refresh(patient)
        return patient
    
    def update(self, patient: Patient):
        db = SessionLocal()
        db.commit()
        db.refresh(patient)
        return patient

    def delete(self, patient: Patient):
        db = SessionLocal()
        db.delete(patient)
        db.commit()


