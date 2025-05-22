from contextlib import contextmanager
from uuid import UUID
from app.auth.entity.auth import Auth
from app.common.datasource import SessionLocal
from app.product.entity.product import Product
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

class ProductRepository:
    def get(self):
        with get_session() as db:
            return db.query(Product).all()
    
    def get_by_id(self, id: UUID):
        with get_session() as db:
            return db.query(Product).filter(Product.id == id).first()
    
    def create(self, product: Product):
        with get_session() as db:
            db.add(product)
            db.flush() 
            db.refresh(product)
            return product
    
    def update(self, product: Product):
        with get_session() as db:
            db.merge(product)
            db.flush()
            db.refresh(product)
            return product

    def delete(self, product: Product):
        with get_session() as db:
            db.delete(product)
