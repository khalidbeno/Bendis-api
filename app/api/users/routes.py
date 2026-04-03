from fastapi import APIRouter
from app.schemas.users import UserProfileResponse, UpdateUserRequest
from app.services.user_service import (
    get_current_user_profile,
    get_all_users,
    update_current_user,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserProfileResponse)
def get_profile():
    return get_current_user_profile()


@router.get("", response_model=list[UserProfileResponse])
def list_users():
    return get_all_users()


@router.put("/me", response_model=UserProfileResponse)
def update_profile(data: UpdateUserRequest):
    return update_current_user(data)