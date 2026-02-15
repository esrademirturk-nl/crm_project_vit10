from fastapi import APIRouter,HTTPException
from backend.schemas.users import UserCreate, UserPublic, LoginRequest,ResetPasswordRequest
from backend.services.users_service import list_users, create_user, login,reset_password
from backend.services.mail_service import send_mail_service
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
def login_api(body: LoginRequest):
    if not SHEET_ID:
        raise HTTPException(status_code=500, detail="USERS_SHEET_ID env missing or .env not loaded")

    return login(sheet_id=SHEET_ID, kullanici=body.kullanici, parola=body.parola)

@router.post("/reset-password")
def reset_password_route(req: ResetPasswordRequest):
    try:
        sheet_id = os.getenv("USERS_SHEET_ID", "").strip()
        if not sheet_id:
            raise RuntimeError("USERS_SHEET_ID env eksik")

        new_password = reset_password(sheet_id, req.username)

        subject = "Yeni Şifreniz"
        body = (
            f"Merhaba {req.username},\n\n"
            f"Yeni şifreniz: {new_password}\n\n"
            f"Lütfen giriş yaptıktan sonra şifrenizi değiştirin."
        )

        send_mail_service(to_email=req.email, subject=subject, body=body)
        return {"ok": True, "message": "Yeni şifre mail ile gönderildi."}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
