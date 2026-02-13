from backend.sheets_db import read_rows, append_row

MENTOR_RANGE = "'Sayfa1'!A1:H"

def list_mentor_raw(sheet_id: str):
    return read_rows(sheet_id, MENTOR_RANGE)

def add_mentor(sheet_id: str, row: list):
    append_row(sheet_id, MENTOR_RANGE, row)
