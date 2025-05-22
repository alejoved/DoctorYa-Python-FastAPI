from contextlib import contextmanager
from uuid import UUID
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
from app.customer.entity.customer import Customer
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

class CustomerRepository:
    def get(self):
        with get_session() as db:
            return db.query(Customer).options(
            joinedload(Customer.auth)).all()
    
    def get_by_id(self, id: UUID):
        with get_session() as db:
            return db.query(Customer).options(joinedload(Customer.auth)).filter(Customer.id == id).first()
    
    def get_by_auth_identification(self, identification: str):
        with get_session() as db:
            return db.query(Customer).options(joinedload(Customer.auth)).filter(Auth.identification == identification).first()
    
    def create(self, customer: Customer):
        with get_session() as db:
            db.add(customer)
            db.flush() 
            db.refresh(customer)
            customer_with_relations = db.query(Customer).options(
            joinedload(Customer.auth)
            ).filter(Customer.id == customer.id).first()
            return customer_with_relations
    
    def update(self, customer: Customer):
        with get_session() as db:
            db.merge(customer)
            db.flush()
            db.refresh(customer)
            return customer

    def delete(self, customer: Customer):
        with get_session() as db:
            db.delete(customer)


