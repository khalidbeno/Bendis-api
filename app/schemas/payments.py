from pydantic import BaseModel, Field


class CreatePaymentRequest(BaseModel):
    order_id: int
    amount: float = Field(..., gt=0)


class PaymentResponse(BaseModel):
    payment_id: int
    order_id: int
    amount: float
    status: str


class ConfirmPaymentRequest(BaseModel):
    payment_id: int


class ConfirmPaymentResponse(BaseModel):
    message: str
    payment_id: int
    status: str