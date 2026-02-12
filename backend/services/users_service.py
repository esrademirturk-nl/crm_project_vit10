from fastapi import HTTPException
from repositories.users_repo import list_users_raw, add_user

def list_users(sheet_id: str):
    values = list_users_raw(sheet_id)
    if not values or len(values) == 1:
        return []

    rows = values[1:]
    result = []
    for r in rows:
        r = (r + ["", "", ""])[:3]
        result.append({"kullanici": r[0], "yetki": r[2]})  # parola dönmüyoruz
    return result

def create_user(sheet_id: str, kullanici: str, parola: str, yetki: str):
    # aynı kullanıcı var mı?
    values = list_users_raw(sheet_id)
    rows = values[1:] if values and len(values) > 1 else []
    for r in rows:
        r = (r + ["", "", ""])[:3]
        if r[0] == kullanici:
            raise HTTPException(status_code=409, detail="Kullanıcı zaten var")

    add_user(sheet_id, kullanici, parola, yetki)
    return {"kullanici": kullanici, "yetki": yetki}

def login(sheet_id: str, kullanici: str, parola: str):
    values = list_users_raw(sheet_id)
    rows = values[1:] if values and len(values) > 1 else []

    for r in rows:
        r = (r + ["", "", ""])[:3]
        if r[0] == kullanici and r[1] == parola:
            return {"ok": True, "kullanici": kullanici, "yetki": r[2]}

    raise HTTPException(status_code=401, detail="Hatalı kullanıcı/parola")
