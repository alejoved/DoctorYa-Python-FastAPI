from uuid import UUID
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
from app.physician.entity.physician import Physician

class PhysicianRepository:
    def get(self):
        db = SessionLocal()
        physicians = db.query(Physician).all()
        return physicians
    
    def get_by_id(self, id: UUID):
        db = SessionLocal()
        physician = db.query(Physician).filter(Physician.id == id).first()
        return physician
    
    def get_by_auth_identification(self, identification: str):
        db = SessionLocal()
        patient = db.query(Physician).join(Physician.auth).filter(Auth.identification == identification).first()
        return patient
    
    def create(self, physician: Physician):
        db = SessionLocal()
        db.add(physician)
        db.commit()
        db.refresh(physician)
        return physician
    
    def update(self, physician: Physician):
        db = SessionLocal()
        db.commit()
        db.refresh(physician)
        return physician

    def delete(self, physician: Physician):
        db = SessionLocal()
        db.delete(physician)
        db.commit()
