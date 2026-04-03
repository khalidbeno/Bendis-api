from app.schemas.payments import (
    CreatePaymentRequest,
    PaymentResponse,
    ConfirmPaymentRequest,
    ConfirmPaymentResponse,
)


def create_payment(data: CreatePaymentRequest) -> PaymentResponse:
    return PaymentResponse(
        payment_id=1,
        order_id=data.order_id,
        amount=data.amount,
        status="pending"
    )


def confirm_payment(data: ConfirmPaymentRequest) -> ConfirmPaymentResponse:
    return ConfirmPaymentResponse(
        message="Payment confirmed successfully",
        payment_id=data.payment_id,
        status="paid"
    )