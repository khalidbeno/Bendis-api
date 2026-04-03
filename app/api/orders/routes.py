from fastapi import APIRouter
from app.schemas.orders import (
    CreateOrderRequest,
    OrderResponse,
    OrderSummaryResponse,
)
from app.services.order_service import (
    create_order,
    get_all_orders,
    get_order_by_id,
)

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderResponse)
def create_new_order(data: CreateOrderRequest):
    return create_order(data)


@router.get("", response_model=list[OrderSummaryResponse])
def list_orders():
    return get_all_orders()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int):
    return get_order_by_id(order_id)