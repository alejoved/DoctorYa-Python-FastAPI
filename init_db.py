from app.common.datasource import Base 
from app.common.datasource import engine
from app.auth.entity.auth import Auth
from app.patient.entity.patient import Patient
from app.physician.entity.physician import Physician
from app.appointment.entity.appointment import Appointment


def init_db():
    print("Tablas registradas:", list(Base.metadata.tables.keys()))
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas")

init_db()