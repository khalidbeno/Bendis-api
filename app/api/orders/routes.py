from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.utils.dependencies import get_current_user
from app.schemas.orders import OrderResponse
from app.services.order_service import (
    create_order_from_cart,
    list_user_orders,
    get_user_order,
)

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderResponse)
def create_order_endpoint(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        return create_order_from_cart(db, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=list[OrderResponse])
def get_orders_endpoint(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return list_user_orders(db, current_user.id)


@router.get("/{order_id}")
def get_order_endpoint(order_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    try:
        return get_user_order(db, current_user.id, order_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))