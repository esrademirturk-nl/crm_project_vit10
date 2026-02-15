from backend.sheets_db import read_rows, append_row, update_cell

USERS_SHEET = "Form Yanıtları 1"
USERS_RANGE = f"'{USERS_SHEET}'!A1:C"

def list_users_raw(sheet_id: str):
    return read_rows(sheet_id, USERS_RANGE)

def add_user(sheet_id: str, kullanici: str, parola_hash: str, yetki: str):
    append_row(sheet_id, USERS_RANGE, [kullanici, parola_hash, yetki])

def find_user_row_index(sheet_id: str, kullanici: str):
    values = list_users_raw(sheet_id) or []
    rows = values[1:] if len(values) > 1 else []
    u_in = (kullanici or "").strip().lower()

    for i, r in enumerate(rows, start=2):  # header=1, ilk data=2
        r = (r + ["", "", ""])[:3]
        u = (r[0] or "").strip().lower()
        if u == u_in:
            return i  # sheet 1-based row index
    return None

def update_password(sheet_id: str, row_index_1based: int, new_password: str):
    cell = f"'Form Yanıtları 1'!B{row_index_1based}"
    update_cell(sheet_id, cell, new_password)
