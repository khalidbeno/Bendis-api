from pydantic import BaseModel, Field


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int


class CreateProductRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=255)
    price: float
    stock: int


class UpdateProductRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=255)
    price: float
    stock: int


class DeleteProductResponse(BaseModel):
    message: str