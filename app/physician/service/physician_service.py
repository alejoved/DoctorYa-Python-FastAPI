from uuid import UUID
from app.common import constants
from app.exception.exception_handler import entity_not_exists_exception
from app.physician.dto.physician_dto import PhysicianDTO, dto_to_physician
from app.physician.dto.physician_response_dto import physician_to_dto
from app.physician.repository.physician_repository import PhysicianRepository

class PhysicianService:

    def __init__(self, physician_repository: PhysicianRepository):
        self.physician_repository = physician_repository
    
    def get(self):
        return self.physician_repository.get()

    def get_by_id(self, id: UUID):
        physician = self.physician_repository.get_by_id(id)
        if not physician:
            raise entity_not_exists_exception(constants.physician_not_found)
        physician_response_dto = physician_to_dto(physician)
        return physician_response_dto
    
    def create(self, physician_dto: PhysicianDTO):
        physician = dto_to_physician(physician_dto)
        physician = self.physician_repository.create(physician)
        physician_response_dto = physician_to_dto(physician)
        return physician_response_dto
    
    def update(self, id: UUID, physician_dto: PhysicianDTO):
        physician = self.physician_repository.get_by_id(id)
        if not physician:
            raise entity_not_exists_exception(constants.physician_not_found)
        physician = dto_to_physician(physician_dto)
        physician = self.physician_repository.update(physician)
        return physician

    def delete(self, id: UUID):
        physician = self.physician_repository.get_by_id(id)
        if not physician:
            raise entity_not_exists_exception(constants.physician_not_found)
        self.physician_repository.delete(physician)