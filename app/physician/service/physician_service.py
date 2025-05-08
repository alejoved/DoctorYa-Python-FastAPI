from uuid import UUID
from app.auth.entity.auth import Auth
from app.auth.repository.auth_repository import AuthRepository
from app.common import constants
from app.common.mapper import Mapper
from app.common.role import Role
from app.exception.exception_handler import entity_exists_exception, entity_not_exists_exception
from app.physician.dto.physician_dto import PhysicianDTO
from app.physician.repository.physician_repository import PhysicianRepository
from passlib.context import CryptContext

class PhysicianService:

    def __init__(self, physician_repository: PhysicianRepository, auth_repository: AuthRepository):
        self.physician_repository = physician_repository
        self.auth_repository = auth_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get(self):
        return self.physician_repository.get()

    def get_by_id(self, id: UUID):
        physician = self.physician_repository.get_by_id(id)
        if not physician:
            raise entity_not_exists_exception(constants.physician_not_found)
        physician_response_dto = Mapper.physician_to_physician_response_dto(physician)
        return physician_response_dto
    
    def create(self, physician_dto: PhysicianDTO):
        authExists = self.auth_repository.get_by_identification(physician_dto.identification)
        if authExists:
            raise entity_exists_exception(constants.auth_exists)
        auth = Auth()
        auth.identification = physician_dto.identification
        auth.password = self.pwd_context.hash(physician_dto.password)
        auth.role = Role.PHYSICIAN
        physician = Mapper.physician_dto_to_physician(physician_dto)
        physician.auth = auth
        physician = self.physician_repository.create(physician)
        physician_response_dto = Mapper.physician_to_physician_response_dto(physician)
        return physician_response_dto
    
    def update(self, id: UUID, physician_dto: PhysicianDTO):
        physician = self.physician_repository.get_by_id(id)
        if not physician:
            raise entity_not_exists_exception(constants.physician_not_found)
        physician = Mapper.physician_dto_to_physician(physician_dto)
        physician = self.physician_repository.update(physician)
        return physician

    def delete(self, id: UUID):
        physician = self.physician_repository.get_by_id(id)
        if not physician:
            raise entity_not_exists_exception(constants.physician_not_found)
        self.physician_repository.delete(physician)