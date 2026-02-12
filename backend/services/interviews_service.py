from repositories.interviews_repo import list_interview_raw, add_interview

def list_interviews(sheet_id: str):
    values = list_interview_raw(sheet_id)
    if not values or len(values) == 1:
        return []

    header = values[0]
    rows = values[1:]

    result = []
    for r in rows:
        result.append(dict(zip(header, r)))
    return result

def create_interview(sheet_id: str, data):
    row = [
        data.ad_soyad,
        data.proje_gonderilis_tarihi,
        data.projenin_gelis_tarihi
    ]
    add_interview(sheet_id, row)
    return {"status": "ok"}
