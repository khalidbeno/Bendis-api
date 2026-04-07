from sqlalchemy.orm import Session

from app.repositories.cart_repository import get_cart_by_user, get_cart_items
from app.repositories.order_repository import (
    create_order,
    create_order_item,
    get_orders_by_user,
    get_order_by_id,
    get_order_items,
    clear_cart,
)


def create_order_from_cart(db: Session, user_id: int):
    cart = get_cart_by_user(db, user_id)

    if not cart:
        raise ValueError("Cart not found")

    cart_items = get_cart_items(db, cart.id)

    if not cart_items:
        raise ValueError("Cart is empty")

    order = create_order(db, user_id)

    for item in cart_items:
        create_order_item(
            db=db,
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )

    clear_cart(db, cart.id)

    return order


def list_user_orders(db: Session, user_id: int):
    return get_orders_by_user(db, user_id)


def get_user_order(db: Session, user_id: int, order_id: int):
    order = get_order_by_id(db, order_id)

    if not order:
        raise ValueError("Order not found")

    if order.user_id != user_id:
        raise ValueError("Not authorized to view this order")

    items = get_order_items(db, order.id)

    return {
        "id": order.id,
        "user_id": order.user_id,
        "status": order.status,
        "items": [
            {
                "id": item.id,
                "product_id": item.product_id,
                "quantity": item.quantity
            }
            for item in items
        ]
    }