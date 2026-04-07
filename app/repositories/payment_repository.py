from sqlalchemy.orm import Session
from app.db.models.payment import Payment


def create_payment(db: Session, order_id: int, amount: float):
    payment = Payment(
        order_id=order_id,
        amount=amount,
        status="paid"
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment