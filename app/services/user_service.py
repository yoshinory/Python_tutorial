from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.repositories.user_repo import fetch_users, save_user, find_user_by_name
from app.exceptions.user_exceptions import UserAlreadyExists
from app.core.logging import logger

def get_users_service(db: Session, limit: int, offset: int):
    return fetch_users(db, limit, offset)

def create_user_service(db: Session, payload: UserCreate):
    logger.info("Creating user: %s", payload.name)
    if find_user_by_name(db, payload.name):
        raise UserAlreadyExists()
    return save_user(db, payload.name)

