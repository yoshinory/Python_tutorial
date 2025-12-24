from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models import User

def fetch_users(db: Session, limit: int, offset: int):
    stmt = select(User).limit(limit).offset(offset)
    return db.execute(stmt).scalars().all()

def save_user(db: Session, name: str):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def find_user_by_name(db: Session, name: str):
    return db.execute(
        select(User).where(User.name == name)
    ).scalar_one_or_none()