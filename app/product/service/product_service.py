from uuid import UUID
from app.auth.entity.auth import Auth
from app.auth.repository.auth_repository import AuthRepository
from app.common import constants
from app.common.mapper import Mapper
from app.common.role import Role
from app.exception.exception_handler import entity_exists_exception, entity_not_exists_exception
from app.product.dto.product_dto import ProductDTO
from app.product.repository.product_repository import ProductRepository
from passlib.context import CryptContext

class ProductService:

    def __init__(self, product_repository: ProductRepository, auth_repository: AuthRepository):
        self.product_repository = product_repository
        self.auth_repository = auth_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def get(self):
        products = self.product_repository.get()
        return [Mapper.product_to_product_response_dto(product) for product in products]

    def get_by_id(self, id: UUID):
        product = self.product_repository.get_by_id(id)
        if not product:
            raise entity_not_exists_exception(constants.product_not_found)
        product_response_dto = Mapper.product_to_product_response_dto(product)
        return product_response_dto
    
    def get_by_identification(self, identification: str):
        product = self.product_repository.get_by_auth_identification(identification)
        if not product:
            raise entity_not_exists_exception(constants.product_not_found)
        product_response_dto = Mapper.product_to_product_response_dto(product)
        return product_response_dto
    
    def create(self, product_dto: ProductDTO):
        authExists = self.auth_repository.get_by_identification(product_dto.identification)
        if authExists:
            raise entity_exists_exception(constants.auth_exists)
        auth = Auth()
        auth.identification = product_dto.identification
        auth.password = self.pwd_context.hash(product_dto.password)
        auth.role = Role.PHYSICIAN
        product = Mapper.product_dto_to_product(product_dto)
        product.auth = auth
        product = self.product_repository.create(product)
        product_response_dto = Mapper.product_to_product_response_dto(product)
        return product_response_dto
    
    def update(self, id: UUID, product_dto: ProductDTO):
        product = self.product_repository.get_by_id(id)
        if not product:
            raise entity_not_exists_exception(constants.product_not_found)
        product = Mapper.product_dto_to_product(product_dto)
        product = self.product_repository.update(product)
        return product

    def delete(self, id: UUID):
        product = self.product_repository.get_by_id(id)
        if not product:
            raise entity_not_exists_exception(constants.product_not_found)
        self.product_repository.delete(product)