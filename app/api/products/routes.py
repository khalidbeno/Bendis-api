from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.products import (
    ProductCreateRequest,
    ProductUpdateRequest,
    ProductResponse,
)
from app.services.product_service import (
    list_products,
    get_product,
    create_new_product,
    update_existing_product,
    delete_existing_product,
)

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return list_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    try:
        return get_product(db, product_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("", response_model=ProductResponse)
def create_product_endpoint(data: ProductCreateRequest, db: Session = Depends(get_db)):
    return create_new_product(
        db=db,
        name=data.name,
        description=data.description,
        price=data.price
    )


@router.put("/{product_id}", response_model=ProductResponse)
def update_product_endpoint(product_id: int, data: ProductUpdateRequest, db: Session = Depends(get_db)):
    try:
        return update_existing_product(
            db=db,
            product_id=product_id,
            name=data.name,
            description=data.description,
            price=data.price
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{product_id}")
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    try:
        delete_existing_product(db, product_id)
        return {"message": "Product deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))