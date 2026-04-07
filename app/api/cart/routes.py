from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.utils.dependencies import get_current_user
from app.schemas.cart import AddToCartRequest
from app.services.cart_service import get_user_cart, add_to_cart, remove_from_cart

router = APIRouter(prefix="/cart", tags=["cart"])


@router.get("")
def get_cart(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return get_user_cart(db, current_user.id)


@router.post("/items")
def add_item(data: AddToCartRequest, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return add_to_cart(
        db=db,
        user_id=current_user.id,
        product_id=data.product_id,
        quantity=data.quantity
    )


@router.delete("/items/{item_id}")
def remove_item(item_id: int, db: Session = Depends(get_db)):
    remove_from_cart(db, item_id)
    return {"message": "Item removed"}