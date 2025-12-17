from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse


router = APIRouter()

_users = [{"id:": 1, "name": "Alice"}]
_next_id = 2

@router.get("/users", response_model=list[UserResponse])
def get_users():
     return _users

@router.post("/users", response_model=UserResponse, status_code=201)
def create_user(payload: UserCreate):
     global _next_id
     user = {"id": _next_id, "name": payload.name}
     _next_id += 1
     _users.append(user)
     return user
