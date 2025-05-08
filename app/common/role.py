from enum import Enum

class Role(str, Enum):
    ADMIN = "ADMIN"
    PATIENT = "PATIENT"
    PHYSICIAN = "PHYSICIAN"