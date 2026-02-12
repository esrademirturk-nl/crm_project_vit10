from sheets_db import read_rows, append_row

USERS_RANGE = "'Form Yanıtları 1'!A1:C" 

def list_users_raw(sheet_id: str):
    return read_rows(sheet_id, USERS_RANGE)

def add_user(sheet_id: str, kullanici: str, parola: str, yetki: str):
    append_row(sheet_id, USERS_RANGE, [kullanici, parola, yetki])