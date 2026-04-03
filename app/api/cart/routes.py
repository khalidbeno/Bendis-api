from fastapi import APIRouter
from app.schemas.cart import (
    CartResponse,
    CartItemResponse,
    AddToCartRequest,
    RemoveFromCartResponse,
)
from app.services.cart_service import (
    get_cart,
    add_item_to_cart,
    remove_item_from_cart,
)

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("", response_model=CartResponse)
def get_user_cart():
    return get_cart()


@router.post("/items", response_model=CartItemResponse)
def add_to_cart(data: AddToCartRequest):
    return add_item_to_cart(data)


@router.delete("/items/{item_id}", response_model=RemoveFromCartResponse)
def remove_from_cart(item_id: int):
    return remove_item_from_cart(item_id)