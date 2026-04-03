from pydantic import BaseModel, EmailStr, Field


class UserProfileResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class UpdateUserRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr