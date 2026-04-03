from app.schemas.cart import (
    CartResponse,
    CartItemResponse,
    AddToCartRequest,
    RemoveFromCartResponse,
)


def get_cart() -> CartResponse:
    return CartResponse(
        items=[
            CartItemResponse(id=1, product_id=1, quantity=2),
            CartItemResponse(id=2, product_id=2, quantity=1),
        ]
    )


def add_item_to_cart(data: AddToCartRequest) -> CartItemResponse:
    return CartItemResponse(
        id=3,
        product_id=data.product_id,
        quantity=data.quantity,
    )


def remove_item_from_cart(item_id: int) -> RemoveFromCartResponse:
    return RemoveFromCartResponse(
        message=f"Item {item_id} removed from cart"
    )