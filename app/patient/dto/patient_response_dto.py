from app.patient.entity.patient import Patient

class PatientResponseDTO:
    name: str
    insurance: str

def patient_to_dto(patient: Patient) -> PatientResponseDTO:
    return PatientResponseDTO(
        id = patient.id,
        insurance = patient.name
    )