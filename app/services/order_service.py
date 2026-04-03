from app.schemas.orders import (
    CreateOrderRequest,
    OrderResponse,
    OrderItemResponse,
    OrderSummaryResponse,
)


def create_order(data: CreateOrderRequest) -> OrderResponse:
    return OrderResponse(
        id=1,
        user_id=data.user_id,
        items=data.items,
        total_price=29.99,
        status="pending"
    )


def get_all_orders() -> list[OrderSummaryResponse]:
    return [
        OrderSummaryResponse(
            id=1,
            total_price=29.99,
            status="pending"
        ),
        OrderSummaryResponse(
            id=2,
            total_price=49.99,
            status="paid"
        )
    ]


def get_order_by_id(order_id: int) -> OrderResponse:
    return OrderResponse(
        id=order_id,
        user_id=1,
        items=[
            OrderItemResponse(product_id=1, quantity=2),
            OrderItemResponse(product_id=2, quantity=1),
        ],
        total_price=29.99,
        status="pending"
    )