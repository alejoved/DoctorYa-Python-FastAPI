from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.auth.repository.auth_repository import AuthRepository
from app.common.role import Role
from app.config.auth_config import valid_role
from app.customer.dto.customer_dto import CustomerDTO
from app.customer.dto.customer_response_dto import CustomerResponseDTO
from app.customer.repository.customer_repository import CustomerRepository
from app.customer.service.customer_service import CustomerService

customer_route = APIRouter()

def get_customer_service():
    customer_repository = CustomerRepository()
    auth_repository = AuthRepository()
    return CustomerService(customer_repository, auth_repository)

@customer_route.get("/api/customer", response_model=List[CustomerResponseDTO], response_model_exclude_none=True, tags=["Customer"],
                   summary="Get all customers currently",
                       responses={200: {"description": "Get all customers successfully"},
                                  500: {"description": "Internal server error"}})
def get(customer_service: CustomerService = Depends(get_customer_service)):
    customer_response_dto = customer_service.get()
    return customer_response_dto

@customer_route.get("/api/customer/{id}", response_model=CustomerResponseDTO, response_model_exclude_none=True, tags=["Customer"],
                    summary="Get an customer existing by uuid",
                    responses={200: {"description": "Get an customer successfully"},
                                404: {"description": "Customer not found"}, 
                                500: {"description": "Internal server error"}})
def get_by_id(id: UUID, customer_service: CustomerService = Depends(get_customer_service)):
    customer_response_dto = customer_service.get_by_id(id)
    return customer_response_dto

@customer_route.get("/api/customer/{id}", response_model=CustomerResponseDTO, response_model_exclude_none=True, tags=["Customer"],
                    summary="Get an customer existing by uuid",
                    responses={200: {"description": "Get an customer successfully"},
                                404: {"description": "Customer not found"}, 
                                500: {"description": "Internal server error"}})
def get_by_id(id: UUID, dep = Depends(valid_role(Role.ADMIN)), customer_service: CustomerService = Depends(get_customer_service)):
    customer_response_dto = customer_service.get_by_id(id)
    return customer_response_dto

@customer_route.get("/api/customer/identification/{identification}", response_model=CustomerResponseDTO, response_model_exclude_none=True, tags=["Customer"],
                    summary="Get an customer existing by identification",
                    responses={200: {"description": "Get an customer by identification successfully"},
                                404: {"description": "Customer not found"}, 
                                500: {"description": "Internal server error"}})
def get_by_identification(identification: str, customer_service: CustomerService = Depends(get_customer_service)):
    customer_response_dto = customer_service.get_by_identification(identification)
    return customer_response_dto

@customer_route.post("/api/customer", response_model=CustomerResponseDTO, response_model_exclude_none=True, tags=["Customer"],
                    summary="Create a new customer associated with a identification, name and an medical code",
                    responses={200: {"description": "Customer created successfully"},
                                409: {"description": "Customer already exists"}, 
                                500: {"description": "Internal server error"}})
def create(customer_dto: CustomerDTO, dep = Depends(valid_role(Role.ADMIN)), customer_service: CustomerService = Depends(get_customer_service)):
    customer_response_dto = customer_service.create(customer_dto)
    return customer_response_dto

@customer_route.put("/api/customer/{id}", response_model=CustomerResponseDTO, response_model_exclude_none=True, tags=["Customer"],
                    summary="Update data about a customer by uuid",
                    responses={200: {"description": "Customer updated successfully"},
                                404: {"description": "Customer not found"}, 
                                500: {"description": "Internal server error"}})
def update(id: UUID, customer_dto: CustomerDTO, customer_service: CustomerService = Depends(get_customer_service)):
    customer_response_dto = customer_service.update(id, customer_dto)
    return customer_response_dto

@customer_route.delete("/api/customer/{id}", tags=["Customer"],
                    summary="Delete an customer by uuid",
                    responses={200: {"description": "Customer deleted successfully"},
                                404: {"description": "Customer not found"}, 
                                500: {"description": "Internal server error"}})
def delete(id: UUID, dep = Depends(valid_role(Role.ADMIN)), customer_service: CustomerService = Depends(get_customer_service)):
    customer_service.delete(id)