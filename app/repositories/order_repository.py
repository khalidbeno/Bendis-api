from sqlalchemy.orm import Session

from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.db.models.cart_item import CartItem


def create_order(db: Session, user_id: int):
    order = Order(user_id=user_id, status="pending")
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def create_order_item(db: Session, order_id: int, product_id: int, quantity: int):
    order_item = OrderItem(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity
    )
    db.add(order_item)
    db.commit()
    db.refresh(order_item)
    return order_item


def get_orders_by_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()


def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def get_order_items(db: Session, order_id: int):
    return db.query(OrderItem).filter(OrderItem.order_id == order_id).all()


def clear_cart(db: Session, cart_id: int):
    db.query(CartItem).filter(CartItem.cart_id == cart_id).delete()
    db.commit()