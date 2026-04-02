from app.schemas.auth import (
    RegisterRequest,
    RegisterResponse,
    LoginRequest,
    LoginResponse,
)


def register_user(data: RegisterRequest) -> RegisterResponse:
    return RegisterResponse(
        message="User registered successfully",
        username=data.username,
        email=data.email
    )

def login_user(data: LoginRequest) -> LoginResponse:
    return LoginResponse(
        message="User logged  in successfully",
        email=data.email
    )