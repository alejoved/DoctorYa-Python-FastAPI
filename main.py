from fastapi import Depends, FastAPI
from app.auth.controller.auth_controller import auth_route
from app.patient.controller.patient_controller import patient_route
from app.physician.controller.physician_controller import physician_route
from app.appointment.controller.appointment_controller import appointment_route

app = FastAPI(
    title="Medical Appointment Booking API",
    description="Medical Appointment Booking API Technical Documentation",
    version="1.0.0"
)

app.include_router(auth_route)
app.include_router(patient_route)
app.include_router(physician_route)
app.include_router(appointment_route)
