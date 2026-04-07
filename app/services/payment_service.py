from sqlalchemy.orm import Session

from app.repositories.order_repository import get_order_by_id
from app.repositories.payment_repository import create_payment


def process_payment(db: Session, user_id: int, order_id: int):
    order = get_order_by_id(db, order_id)

    if not order:
        raise ValueError("Order not found")

    if order.user_id != user_id:
        raise ValueError("Not authorized")

    if order.status == "paid":
        raise ValueError("Order already paid")

    # Aquí podrías calcular total real (de momento fake)
    amount = 100.0

    payment = create_payment(db, order_id, amount)

    order.status = "paid"
    db.commit()

    return payment