from googleapiclient.discovery import build
from backend.auth import auth

_service = None  # cache

def sheets_service():
    global _service
    if _service is None:
        creds = auth()  # auth() token.json kullanmalı (ilk sefer hariç)
        _service = build("sheets", "v4", credentials=creds, cache_discovery=False)
    return _service

def read_rows(spreadsheet_id: str, range_a1: str):
    svc = sheets_service()
    resp = svc.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_a1
    ).execute()
    return resp.get("values", [])

def append_row(spreadsheet_id: str, range_a1: str, row_values: list):
    svc = sheets_service()
    svc.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_a1,
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body={"values": [row_values]}
    ).execute()
