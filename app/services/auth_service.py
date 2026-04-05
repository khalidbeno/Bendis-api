from sqlalchemy.orm import Session

from app.repositories.user_repository import get_user_by_email, create_user
from app.core.security import hash_password, verify_password


def register_user(db: Session, username: str, email: str, password: str):
    existing_user = get_user_by_email(db, email)

    if existing_user:
        raise ValueError("User already exists")

    hashed_password = hash_password(password)

    user = create_user(
        db=db,
        username=username,
        email=email,
        password=hashed_password
    )

    return user


def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        raise ValueError("Invalid credentials")

    if not verify_password(password, user.password):
        raise ValueError("Invalid credentials")

    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }