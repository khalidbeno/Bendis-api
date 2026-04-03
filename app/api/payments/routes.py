from fastapi import APIRouter
from app.schemas.payments import (
    CreatePaymentRequest,
    PaymentResponse,
    ConfirmPaymentRequest,
    ConfirmPaymentResponse,
)
from app.services.payment_service import create_payment, confirm_payment

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("", response_model=PaymentResponse)
def create_new_payment(data: CreatePaymentRequest):
    return create_payment(data)


@router.post("/confirm", response_model=ConfirmPaymentResponse)
def confirm_existing_payment(data: ConfirmPaymentRequest):
    return confirm_payment(data)