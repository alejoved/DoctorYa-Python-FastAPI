import uuid
from sqlalchemy import UUID, Column, DateTime, ForeignKey, String
from app.common.datasource import Base
from sqlalchemy.orm import relationship

from app.patient.entity.patient import Patient
from app.physician.entity.physician import Physician

class Appointment(Base):
    __tablename__ = "appointment"
    __table_args__ = {"schema": "doctoryapython"}

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    reason = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    patient_id = Column(UUID(as_uuid=True), ForeignKey(Patient.id))
    patient = relationship('Patient')

    physician_id = Column(UUID(as_uuid=True), ForeignKey(Physician.id))
    physician = relationship('Physician')