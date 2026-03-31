from fastapi import FastAPI
from app.api.routes import router as main_router
from app.api.auth.routes import router as auth_router

app = FastAPI()

app.include_router(main_router)
app.include_router(auth_router)