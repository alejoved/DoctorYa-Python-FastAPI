from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.auth.repository.auth_repository import AuthRepository
from app.product.dto.product_dto import ProductDTO
from app.product.dto.product_response_dto import ProductResponseDTO
from app.product.repository.product_repository import ProductRepository
from app.product.service.product_service import ProductService

product_route = APIRouter()

def get_product_service():
    product_repository = ProductRepository()
    auth_repository = AuthRepository()
    return ProductService(product_repository, auth_repository)

@product_route.get("/api/product", response_model=List[ProductResponseDTO], response_model_exclude_none=True, tags=["Product"],
                    summary="Get all products currently",
                    responses={200: {"description": "Get all the products Successfully"},
                                500: {"description": "Internal server error"}})
def get(product_service: ProductService = Depends(get_product_service)):
    product_response_dto = product_service.get()
    return product_response_dto

@product_route.get("/api/product/{id}", response_model=ProductResponseDTO, response_model_exclude_none=True, tags=["Product"],
                    summary="Get an product existing by uuid",
                    responses={200: {"description": "Get an product successfully"},
                                404: {"description": "Product not found"}, 
                                500: {"description": "Internal server error"}})
def get_by_id(id: UUID, product_service: ProductService = Depends(get_product_service)):
    product_response_dto = product_service.get_by_id(id)
    return product_response_dto

@product_route.get("/api/product/identification/{identification}", response_model=ProductResponseDTO, response_model_exclude_none=True, tags=["Product"],
                    summary="Get an product existing by identification",
                    responses={200: {"description": "Get an product by identification successfully"},
                                404: {"description": "Product not found"}, 
                                500: {"description": "Internal server error"}})
def get_by_identification(identification: str, product_service: ProductService = Depends(get_product_service)):
    product_response_dto = product_service.get_by_identification(identification)
    return product_response_dto

@product_route.post("/api/product", response_model=ProductResponseDTO, response_model_exclude_none=True, tags=["Product"],
                    summary="Create a new product associated with a name and medical code",
                    responses={200: {"description": "Product created successfully"},
                                404: {"description": "Product not found"}, 
                                500: {"description": "Internal server error"}})
def create(product_dto: ProductDTO, product_service: ProductService = Depends(get_product_service)):
    product_response_dto = product_service.create(product_dto)
    return product_response_dto

@product_route.put("/api/product/{id}", response_model=ProductResponseDTO, response_model_exclude_none=True, tags=["Product"],
                    summary="Update data about a product by uuid",
                    responses={200: {"description": "Product updated successfully"},
                                404: {"description": "Product not found"}, 
                                500: {"description": "Internal server error"}})
def update(id: UUID, product_dto: ProductDTO, product_service: ProductService = Depends(get_product_service)):
    product_response_dto = product_service.update(id, product_dto)
    return product_response_dto

@product_route.delete("/api/product/{id}", tags=["Product"],
                    summary="",
                    responses={200: {"description": "Product updated successfully"},
                                404: {"description": "Product not found"}, 
                                500: {"description": "Internal server error"}})
def delete(id: UUID, product_service: ProductService = Depends(get_product_service)):
    product_service.delete(id)