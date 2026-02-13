from backend.sheets_db import read_rows, append_row

APPLICATIONS_RANGE = "'BASVURULAR'!A1:V"

APPLICATION_SHEETS = {
    "all": "BASVURULAR",
    "vit1": "VIT1",
    "vit2": "VIT2",
}

def _range_for(sheet_name: str) -> str:
    return f"'{sheet_name}'!A1:V"

def list_applications_raw(sheet_id: str, tab_key: str = "all"):
    sheet_name = APPLICATION_SHEETS.get(tab_key)
    if not sheet_name:
        raise ValueError(f"Unknown tab_key: {tab_key}")

    range_a1 = _range_for(sheet_name)
    return read_rows(sheet_id, range_a1)


def add_application(sheet_id: str, row: list):
    append_row(sheet_id, APPLICATIONS_RANGE, row)