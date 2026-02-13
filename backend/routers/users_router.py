from fastapi import APIRouter
from backend.schemas.users import UserCreate, UserPublic, LoginRequest
from backend.services.users_service import list_users, create_user, login
import os
from dotenv import load_dotenv

router = APIRouter(prefix="/users", tags=["users"])

load_dotenv()  
SHEET_ID = os.getenv("USERS_SHEET_ID")


@router.get("", response_model=list[UserPublic])
def get_users():
    return list_users(SHEET_ID)

@router.post("", response_model=UserPublic)
def add(data: UserCreate):
    return create_user(SHEET_ID, data.kullanici, data.parola, data.yetki)

@router.post("/login")
def do_login(data: LoginRequest):
    return login(SHEET_ID, data.kullanici, data.parola)
