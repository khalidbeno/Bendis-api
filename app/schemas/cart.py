from pydantic import BaseModel, Field


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int


class CartResponse(BaseModel):
    items: list[CartItemResponse]


class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class RemoveFromCartResponse(BaseModel):
    message: str