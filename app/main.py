from fastapi import FastAPI
from app.routers import users

app = FastAPI()

@app.get("/")
def health():
    return{"status": "ok"}

app.include_router(users.router)