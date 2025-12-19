from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.db.deps import get_db
from app.services.user_service import get_users_service, create_user_service


router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
     return get_users_service(db)

@router.post("", response_model=UserResponse, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):

     return create_user_service(db, payload,)
