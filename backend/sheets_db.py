from googleapiclient.discovery import build
from auth import auth

def sheets_service():
    creds = auth()
    return build("sheets", "v4", credentials=creds)

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
