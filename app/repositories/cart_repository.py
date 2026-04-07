from sqlalchemy.orm import Session
from app.db.models.cart import Cart
from app.db.models.cart_item import CartItem


def get_cart_by_user(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).first()


def create_cart(db: Session, user_id: int):
    cart = Cart(user_id=user_id)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return cart


def get_cart_items(db: Session, cart_id: int):
    return db.query(CartItem).filter(CartItem.cart_id == cart_id).all()


def add_product_to_cart(db: Session, cart_id: int, product_id: int, quantity: int):
    item = CartItem(
        cart_id=cart_id,
        product_id=product_id,
        quantity=quantity
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def remove_cart_item(db: Session, item_id: int):
    item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()