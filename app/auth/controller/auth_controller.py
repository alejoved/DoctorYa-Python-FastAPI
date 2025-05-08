from uuid import UUID
from fastapi import APIRouter, Depends

from app.auth.dto.login_dto import LoginDTO
from app.auth.dto.register_dto import RegisterDTO
from app.auth.repository.auth_repository import AuthRepository
from app.auth.service.auth_service import AuthService

auth_route = APIRouter()

def get_auth_service():
    auth_repository = AuthRepository()
    return AuthService(auth_repository)

@auth_route.post("/api/auth/register")
def register(register_dto: RegisterDTO, auth_service: AuthService = Depends(get_auth_service)):
    register_response_dto = auth_service.register(register_dto)
    return register_response_dto

@auth_route.post("/api/auth/login")
def login(login_dto: LoginDTO, auth_service: AuthService = Depends(get_auth_service)):
    login_response_dto = auth_service.login(login_dto)
    return login_response_dto