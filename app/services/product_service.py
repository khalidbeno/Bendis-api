from sqlalchemy.orm import Session

from app.repositories.product_repository import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
)


def list_products(db: Session):
    return get_all_products(db)


def get_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    if not product:
        raise ValueError("Product not found")

    return product


def create_new_product(db: Session, name: str, description: str, price: float):
    return create_product(db, name, description, price)


def update_existing_product(db: Session, product_id: int, name: str, description: str, price: float):
    product = get_product_by_id(db, product_id)

    if not product:
        raise ValueError("Product not found")

    return update_product(db, product, name, description, price)


def delete_existing_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    if not product:
        raise ValueError("Product not found")

    delete_product(db, product)