from contextlib import contextmanager
from uuid import UUID
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
from app.invoice.entity.invoice import Invoice
from sqlalchemy.orm import joinedload
from app.invoice_detail.entity.invoice_detail import InvoiceDetail

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
            return db.query(Invoice).options(joinedload(Invoice.details).joinedload(InvoiceDetail.product)).all()
    
    def get_by_id(self, id: UUID):
        with get_session() as db:
            return db.query(Invoice).filter(Invoice.id == id).first()
    
    def create(self, invoice: Invoice):
        with get_session() as db:
            db.add(invoice)
            db.flush()
            db.refresh(invoice)
            invoice_with_relations = db.query(Invoice).options(
            joinedload(Invoice.details).joinedload(InvoiceDetail.product)
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