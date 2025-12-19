from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.repositories.user_repo import fetch_users, save_user

def get_users_service(db: Session):
    return fetch_users(db)

def create_user_service(db: Session, payload: UserCreate):
    return save_user(db, payload.name)
