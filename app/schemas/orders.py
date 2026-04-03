from pydantic import BaseModel


class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int


class OrderResponse(BaseModel):
    id: int
    user_id: int
    items: list[OrderItemResponse]
    total_price: float
    status: str


class CreateOrderRequest(BaseModel):
    user_id: int
    items: list[OrderItemResponse]


class OrderSummaryResponse(BaseModel):
    id: int
    total_price: float
    status: str