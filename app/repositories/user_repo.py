from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.models import User

def fetch_users(db: Session):
    return db.execute(select(User)).scalars().all()

def save_user(db: Session, name: str):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
