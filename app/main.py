from fastapi import FastAPI
from app.routers import users
from app.db.session import engine
from app.db.models import Base

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

app.include_router(users.router)