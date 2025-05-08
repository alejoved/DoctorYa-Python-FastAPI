from app.auth.entity.auth import Auth
from app.common import constants
from app.common.mapper import Mapper
from app.common.role import Role
from app.config.auth_config import create_token
from app.exception.exception_handler import credentials_not_valid_exception, entity_exists_exception, entity_not_exists_exception
from app.auth.dto.login_dto import LoginDTO
from app.auth.dto.register_dto import RegisterDTO
from app.auth.repository.auth_repository import AuthRepository
from passlib.context import CryptContext

class AuthService:

    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def register(self, register_dto: RegisterDTO):
        authFound = self.auth_repository.get_by_identification(register_dto.identification)
        if authFound:
            raise entity_exists_exception(constants.auth_exists)
        password = self.pwd_context.hash(register_dto.password)
        auth = Auth()
        auth.identification = register_dto.identification
        auth.password = password
        auth.role = Role.ADMIN
        self.auth_repository.create(auth)
        register_response_dto = Mapper.auth_to_register_response_dto(auth)
        return register_response_dto

    def login(self, login_dto: LoginDTO):
        auth = self.auth_repository.get_by_identification(login_dto.identification)
        if not auth:
            raise entity_not_exists_exception(constants.auth_not_found)
        if not self.pwd_context.verify(login_dto.password, auth.password):
            raise credentials_not_valid_exception(constants.credentials_not_valid);
        token = create_token(auth.identification, auth.role)
        login_response_dto = Mapper.login_to_login_response_dto(token, auth.role)
        return login_response_dto