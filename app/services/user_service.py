from app.schemas.users import UserProfileResponse, UpdateUserRequest


def get_current_user_profile() -> UserProfileResponse:
    return UserProfileResponse(
        id=1,
        username="khaled",
        email="khaled@gmail.com"
    )


def get_all_users() -> list[UserProfileResponse]:
    return [
        UserProfileResponse(
            id=1,
            username="khaled",
            email="khaled@gmail.com"
        ),
        UserProfileResponse(
            id=2,
            username="admin",
            email="admin@gmail.com"
        )
    ]


def update_current_user(data: UpdateUserRequest) -> UserProfileResponse:
    return UserProfileResponse(
        id=1,
        username=data.username,
        email=data.email
    )