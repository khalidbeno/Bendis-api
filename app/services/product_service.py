from app.schemas.products import (
    ProductResponse,
    CreateProductRequest,
    UpdateProductRequest,
    DeleteProductResponse,
)


def get_all_products() -> list[ProductResponse]:
    return [
        ProductResponse(
            id=1,
            name="Bendis Fresh",
            description="Urinal deodorizer with fresh scent",
            price=9.99,
            stock=100
        ),
        ProductResponse(
            id=2,
            name="Bendis Citrus",
            description="Urinal deodorizer with citrus scent",
            price=10.99,
            stock=80
        )
    ]


def get_product_by_id(product_id: int) -> ProductResponse:
    return ProductResponse(
        id=product_id,
        name="Bendis Fresh",
        description="Urinal deodorizer with fresh scent",
        price=9.99,
        stock=100
    )


def create_product(data: CreateProductRequest) -> ProductResponse:
    return ProductResponse(
        id=3,
        name=data.name,
        description=data.description,
        price=data.price,
        stock=data.stock
    )


def update_product(product_id: int, data: UpdateProductRequest) -> ProductResponse:
    return ProductResponse(
        id=product_id,
        name=data.name,
        description=data.description,
        price=data.price,
        stock=data.stock
    )


def delete_product(product_id: int) -> DeleteProductResponse:
    return DeleteProductResponse(
        message=f"Product with id {product_id} deleted successfully"
    )