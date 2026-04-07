from pydantic import BaseModel


class PaymentRequest(BaseModel):
    order_id: int


class PaymentResponse(BaseModel):
    id: int
    order_id: int
    amount: float
    status: str

    class Config:
        from_attributes = True