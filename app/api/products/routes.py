from fastapi import APIRouter
from app.schemas.products import (
    ProductResponse,
    CreateProductRequest,
    UpdateProductRequest,
    DeleteProductResponse,
)
from app.services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
)

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[ProductResponse])
def list_products():
    return get_all_products()


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    return get_product_by_id(product_id)


@router.post("", response_model=ProductResponse)
def create_new_product(data: CreateProductRequest):
    return create_product(data)


@router.put("/{product_id}", response_model=ProductResponse)
def update_existing_product(product_id: int, data: UpdateProductRequest):
    return update_product(product_id, data)


@router.delete("/{product_id}", response_model=DeleteProductResponse)
def delete_existing_product(product_id: int):
    return delete_product(product_id)