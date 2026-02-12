from sheets_db import read_rows, append_row

INTERVIEW_RANGE = "'Sayfa1'!A1:C"

def list_interview_raw(sheet_id: str):
    return read_rows(sheet_id, INTERVIEW_RANGE)

def add_interview(sheet_id: str, row: list):
    append_row(sheet_id, INTERVIEW_RANGE, row)