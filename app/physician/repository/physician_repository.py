from contextlib import contextmanager
from uuid import UUID
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
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

class PhysicianRepository:
    def get(self):
        with get_session() as db:
            return db.query(Physician).all()
    
    def get_by_id(self, id: UUID):
        with get_session() as db:
            return db.query(Physician).filter(Physician.id == id).first()
    
    def get_by_auth_identification(self, identification: str):
        with get_session() as db:
            return db.query(Physician).join(Physician.auth).filter(Auth.identification == identification).first()
    
    def create(self, physician: Physician):
        with get_session() as db:
            db.add(physician)
            db.flush() 
            db.refresh(physician)
            return physician
    
    def update(self, physician: Physician):
        with get_session() as db:
            db.merge(physician)
            db.flush()
            db.refresh(physician)
            return physician

    def delete(self, physician: Physician):
        with get_session() as db:
            db.delete(physician)
