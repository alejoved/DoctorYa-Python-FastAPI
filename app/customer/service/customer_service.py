from uuid import UUID
from app.auth.entity.auth import Auth
from app.auth.repository.auth_repository import AuthRepository
from app.common import constants
from app.common.mapper import Mapper
from app.common.role import Role
from app.exception.exception_handler import entity_exists_exception, entity_not_exists_exception
from app.customer.dto.customer_dto import CustomerDTO
from app.customer.repository.customer_repository import CustomerRepository
from passlib.context import CryptContext

class CustomerService:

    def __init__(self, customer_repository: CustomerRepository, auth_repository: AuthRepository):
        self.customer_repository = customer_repository
        self.auth_repository = auth_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get(self):
        customers = self.customer_repository.get()
        customer_response_dto = [Mapper.customer_to_customer_response_dto(customer) for customer in customers]
        return customer_response_dto

    def get_by_id(self, id: UUID):
        customer = self.customer_repository.get_by_id(id)
        if not customer:
            raise entity_not_exists_exception(constants.customer_not_found)
        customer_response_dto = Mapper.customer_to_customer_response_dto(customer)
        return customer_response_dto
    
    def get_by_identification(self, identification: str):
        customer = self.customer_repository.get_by_auth_identification(identification)
        if not customer:
            raise entity_not_exists_exception(constants.customer_not_found)
        customer_response_dto = Mapper.customer_to_customer_response_dto(customer)
        return customer_response_dto
    
    def create(self, customer_dto: CustomerDTO):
        authExists = self.auth_repository.get_by_identification(customer_dto.identification)
        if authExists:
            raise entity_exists_exception(constants.auth_exists)
        auth = Auth()
        auth.identification = customer_dto.identification
        auth.password = self.pwd_context.hash(customer_dto.password)
        auth.role = Role.PATIENT
        customer = Mapper.customer_dto_to_customer(customer_dto)
        customer.auth = auth
        customer = self.customer_repository.create(customer)
        customer_response_dto = Mapper.customer_to_customer_response_dto(customer)
        return customer_response_dto
    
    def update(self, id: UUID, customer_dto: CustomerDTO):
        customer = self.customer_repository.get_by_id(id)
        if not customer:
            raise entity_not_exists_exception(constants.customer_not_found)
        customer = Mapper.customer_dto_to_customer(customer_dto)
        customer = self.customer_repository.update(customer)
        return customer

    def delete(self, id: UUID):
        customer = self.customer_repository.get_by_id(id)
        if not customer:
            raise entity_not_exists_exception(constants.customer_not_found)
        self.customer_repository.delete(customer)

