
from fastapi import APIRouter
from app.auth.jwt_handler import create_access_token

router = APIRouter()

@router.post("/login")
def login():
    token = create_access_token({"user": "admin"})
    return {"access_token": token}
