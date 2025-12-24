from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.user_exceptions import UserAlreadyExists
from app.routers import users
from app.db.session import engine
from app.db.models import Base
from app.db.models import User
from dotenv import load_dotenv
import app.db.models

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 FastAPI 正常終了")

@app.get("/")
def health():
    return{"status": "ok"}

@app.exception_handler(UserAlreadyExists)
def user_already_exists_handler(
    request: Request, exc: UserAlreadyExists
):
    return JSONResponse(
        status_code=409,
        content={"detail": "User already exists"}
    )

app.include_router(users.router)
load_dotenv()