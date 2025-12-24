from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.exceptions.user_exceptions import UserAlreadyExists

from app.services.user_service import (
    get_users_service,
    create_user_service,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserResponse])
def get_users(
    limit: int = 20,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    return get_users_service(db, limit, offset)


@router.post("", response_model=UserResponse, status_code=201)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_user_service(db, payload)
    except UserAlreadyExists:
        raise HTTPException(status_code=409, detail="User already exists")
