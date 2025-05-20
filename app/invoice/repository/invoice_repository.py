from contextlib import contextmanager
from uuid import UUID
from sqlalchemy.orm import joinedload
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
from app.invoice.entity.invoice import Invoice
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

class InvoiceRepository:
    def get(self):
        with get_session() as db:
            return db.query(Invoice).all()
    
    def get_by_id(self, id: UUID):
        with get_session() as db:
            return db.query(Invoice).filter(Invoice.id == id).first()
    
    def find_overlapping(self, start_date, end_date, physician_identification: str):
        with get_session() as db:
            return db.query(Invoice).join(Invoice.physician).join(Physician.auth).filter(
            Invoice.start_date < end_date,
            Invoice.end_date > start_date,
            Auth.identification == physician_identification
            ).all()
    
    def create(self, invoice: Invoice):
        with get_session() as db:
            db.add(invoice)
            db.flush()
            invoice_with_relations = db.query(Invoice).options(
            joinedload(Invoice.patient).joinedload(Patient.auth),
            joinedload(Invoice.physician).joinedload(Physician.auth)
            ).filter(Invoice.id == invoice.id).first()
            return invoice_with_relations
    
    def update(self, invoice: Invoice):
        with get_session() as db:
            db.merge(invoice)
            db.flush()
            db.refresh(invoice)
            return invoice

    def delete(self, invoice: Invoice):
        with get_session() as db:
            db.delete(invoice)