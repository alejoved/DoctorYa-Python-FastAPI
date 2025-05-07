from app.common import constants
from app.common.datasource import SessionLocal
from app.exception.exception_handler import entity_not_exists_exception
from app.physician.entity.physician import Physician

class PhysicianRepository:
    def get():
        db = SessionLocal()
        physicians = db.query(Physician).all()
        return physicians
    
    def get_by_id(id: str):
        db = SessionLocal()
        physician = db.query(Physician).filter(Physician.id == id).first()
        return physician
    
    def create(physician: Physician):
        db = SessionLocal()
        db.add(physician)
        db.commit()
        db.refresh(physician)
        return physician
    
    def update(physician: Physician):
        db = SessionLocal()
        db.commit()
        db.refresh(physician)

    def delete(physician: Physician):
        db = SessionLocal()
        db.delete(physician)
        db.commit()
