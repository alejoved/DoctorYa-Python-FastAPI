from fastapi import Depends, FastAPI
from app.patient.controller.patient_controller import patient_route

app = FastAPI(
    title="DoctorYa Python - FastAPI",
    description="API sobre el framework FastAPI",
    version="0.0.1"
)

app.include_router(patient_route)
