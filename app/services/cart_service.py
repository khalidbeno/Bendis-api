from sqlalchemy.orm import Session

from app.repositories.cart_repository import (
    get_cart_by_user,
    create_cart,
    get_cart_items,
    add_product_to_cart,
    remove_cart_item
)


def get_user_cart(db: Session, user_id: int):
    cart = get_cart_by_user(db, user_id)

    if not cart:
        cart = create_cart(db, user_id)

    items = get_cart_items(db, cart.id)

    return {
        "cart_id": cart.id,
        "items": items
    }


def add_to_cart(db: Session, user_id: int, product_id: int, quantity: int):
    cart = get_cart_by_user(db, user_id)

    if not cart:
        cart = create_cart(db, user_id)

    return add_product_to_cart(db, cart.id, product_id, quantity)


def remove_from_cart(db: Session, item_id: int):
    remove_cart_item(db, item_id)