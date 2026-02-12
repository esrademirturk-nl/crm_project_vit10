from sheets_db import read_rows, append_row

APPLICATIONS_RANGE = "'Sayfa1'!A1:V"

def list_applications_raw(sheet_id: str):
    return read_rows(sheet_id, APPLICATIONS_RANGE)

def add_application(sheet_id: str, row: list):
    append_row(sheet_id, APPLICATIONS_RANGE, row)