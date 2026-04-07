from pydantic import BaseModel, Field, EmailStr


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str