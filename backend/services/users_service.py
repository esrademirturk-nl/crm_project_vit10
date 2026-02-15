from fastapi import HTTPException
from backend.repositories.users_repo import (
    list_users_raw,
    add_user,
    find_user_row_index,
    update_password
)

def _norm(s: str) -> str:
    return (s or "").strip()

def list_users(sheet_id: str):
    values = list_users_raw(sheet_id)
    if not values or len(values) == 1:
        return []

    rows = values[1:]
    result = []
    for r in rows:
        r = (r + ["", "", ""])[:3]
        result.append({"kullanici": r[0], "yetki": r[2]})
    return result


def create_user(sheet_id: str, kullanici: str, parola: str, yetki: str):
    values = list_users_raw(sheet_id) or []
    rows = values[1:] if len(values) > 1 else []

    u_new = _norm(kullanici)

    for r in rows:
        r = (r + ["", "", ""])[:3]
        if _norm(r[0]).lower() == u_new.lower():
            raise HTTPException(status_code=409, detail="Kullanıcı zaten var")

    # ✅ DÜZ yazıyoruz
    add_user(sheet_id, u_new, _norm(parola), _norm(yetki) or "user")

    return {"kullanici": u_new, "yetki": _norm(yetki) or "user"}


def login(sheet_id: str, kullanici: str, parola: str):
    values = list_users_raw(sheet_id) or []
    rows = values[1:] if len(values) > 1 else []

    u_in = _norm(kullanici).lower()
    p_in = _norm(parola)

    for r in rows:
        r = (r + ["", "", ""])[:3]
        u = _norm(r[0]).lower()
        p = _norm(r[1])
        yetki = _norm(r[2]) or "user"

        # ✅ düz karşılaştırma
        if u == u_in and p == p_in:
            return {"ok": True, "kullanici": r[0], "yetki": yetki}

    raise HTTPException(status_code=401, detail="Hatalı kullanıcı/parola")


def reset_password(sheet_id: str, kullanici: str) -> str:
    row_index = find_user_row_index(sheet_id, kullanici)
    if not row_index:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")

    import secrets, string
    alphabet = string.ascii_letters + string.digits
    new_password = "".join(secrets.choice("0123456789") for _ in range(6))
    update_password(sheet_id, row_index, new_password)

    return new_password
