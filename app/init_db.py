from app.common.datasource import Base 
from app.common.datasource import engine
from app.auth.entity.auth import Auth
from app.customer.entity.customer import Customer
from app.product.entity.product import Product
from app.invoice_detail.entity.invoice_detail import InvoiceDetail
from app.invoice.entity.invoice import Invoice


def init_db():
    print("Tablas registradas:", list(Base.metadata.tables.keys()))
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas")