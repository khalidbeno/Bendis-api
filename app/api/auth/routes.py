from fastapi import APIRouter
# Validacion de datos
from app.schemas.auth import (
    RegisterRequest,
    RegisterResponse,
    LoginRequest,
    LoginResponse,
)
# Logica
from app.services.auth_service import register_user, login_user


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=RegisterResponse)
def register(data: RegisterRequest):
    return register_user(data)


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    return login_user(data)