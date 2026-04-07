from pydantic import BaseModel, Field


class ProductCreateRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., min_length=2, max_length=255)
    price: float = Field(..., gt=0)


class ProductUpdateRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., min_length=2, max_length=255)
    price: float = Field(..., gt=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True