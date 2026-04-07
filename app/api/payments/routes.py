from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.utils.dependencies import get_current_user
from app.schemas.payments import PaymentRequest, PaymentResponse
from app.services.payment_service import process_payment

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("", response_model=PaymentResponse)
def pay_order(data: PaymentRequest, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        return process_payment(
            db=db,
            user_id=current_user.id,
            order_id=data.order_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))