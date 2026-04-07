from fastapi import FastAPI

from app.api.routes import router as main_router

from app.api.auth.routes import router as auth_router
from app.api.users.routes import router as users_router

from app.api.products.routes import router as products_router
from app.api.cart.routes import router as cart_router
from app.api.orders.routes import router as orders_router
from app.api.payments.routes import router as payments_router


from app.db.base import Base
from app.db.session import engine

from app.db.models.user import User
from app.db.models.product import Product
from app.db.models.cart import Cart
from app.db.models.cart_item import CartItem
from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.db.models.payment import Payment

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(main_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(cart_router)
app.include_router(orders_router)
app.include_router(payments_router)
app.include_router(users_router)