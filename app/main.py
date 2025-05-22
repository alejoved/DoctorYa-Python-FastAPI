from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from app.auth.controller.auth_controller import auth_route
from app.customer.controller.customer_controller import customer_route
from app.product.controller.product_controller import product_route
from app.invoice.controller.invoice_controller import invoice_route

app = FastAPI(
    title="Invoice Generation API",
    description="Invoice Generation API Technical Documentation",
    version="1.0.0"
)

app.include_router(auth_route)
app.include_router(customer_route)
app.include_router(product_route)
app.include_router(invoice_route)
