from fastapi import FastAPI
from app.api.routes import router as main_router
from app.api.auth.routes import router as auth_router
from app.api.users.routes import router as users_router
from app.api.products.routes import router as products_router
from app.api.cart.routes import router as cart_router
from app.api.orders.routes import router as orders_router
from app.api.payments.routes import router as payments_router

app = FastAPI()

app.include_router(main_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)
app.include_router(cart_router)
app.include_router(orders_router)
app.include_router(payments_router)