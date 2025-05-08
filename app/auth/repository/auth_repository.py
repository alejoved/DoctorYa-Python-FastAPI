from app.common.datasource import SessionLocal
from app.auth.entity.auth import Auth

class AuthRepository:
    def get(self):
        db = SessionLocal()
        physicians = db.query(Auth).all()
        return physicians
    
    def get_by_identification(self, identification: str):
        db = SessionLocal()
        auth = db.query(Auth).filter(Auth.identification == identification).first()
        return auth
    
    def create(self, auth: Auth):
        db = SessionLocal()
        db.add(auth)
        db.commit()
        db.refresh(auth)
        return auth
    
    def update(self, auth: Auth):
        db = SessionLocal()
        db.commit()
        db.refresh(auth)
        return auth

    def delete(self, auth: Auth):
        db = SessionLocal()
        db.delete(auth)
        db.commit()
