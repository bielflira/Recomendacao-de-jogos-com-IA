from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user: User):
    return {"msg": "Usuário criado"}

@router.post("/login")
def login(user: User):
    return {"token": "fake-jwt-token"}
