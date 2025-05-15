from uuid import UUID
from fastapi import APIRouter, Depends

from app.auth.dto.login_dto import LoginDTO
from app.auth.dto.login_response_dto import LoginResponseDTO
from app.auth.dto.register_dto import RegisterDTO
from app.auth.dto.register_response_dto import RegisterResponseDTO
from app.auth.repository.auth_repository import AuthRepository
from app.auth.service.auth_service import AuthService

auth_route = APIRouter()

def get_auth_service():
    auth_repository = AuthRepository()
    return AuthService(auth_repository)

@auth_route.post("/api/auth/register", response_model=RegisterResponseDTO, response_model_exclude_none=True, tags=["Auth"],
                summary="Sign in with credentials, identification and password",
                responses={200: {"description": "Login successfully"},
                            404: {"description": "Identification or password not match"}, 
                            500: {"description": "Internal server error"}})
def register(register_dto: RegisterDTO, auth_service: AuthService = Depends(get_auth_service)):
    register_response_dto = auth_service.register(register_dto)
    return register_response_dto

@auth_route.post("/api/auth/login", response_model=LoginResponseDTO, response_model_exclude_none=True, tags=["Auth"],
                summary="Sign up with credentials, identification and password",
                responses={200: {"description": "Register credentials successfully"},
                            409: {"description": "User already exists"}, 
                            500: {"description": "Internal server error"}})
def login(login_dto: LoginDTO, auth_service: AuthService = Depends(get_auth_service)):
    login_response_dto = auth_service.login(login_dto)
    return login_response_dto