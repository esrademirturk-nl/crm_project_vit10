from pydantic import BaseModel

class UserCreate(BaseModel):
    kullanici: str
    parola: str
    yetki: str

class UserPublic(BaseModel):
    kullanici: str
    yetki: str

class LoginRequest(BaseModel):
    kullanici: str
    parola: str
