from repositories.mentors_repo import list_mentor_raw, add_mentor

def list_mentors(sheet_id: str):
    values = list_mentor_raw(sheet_id)
    if not values or len(values) == 1:
        return []

    header = values[0]
    rows = values[1:]

    result = []
    for r in rows:
        result.append(dict(zip(header, r)))

    return result


def create_mentor(sheet_id: str, data):
    row = [
        data.gorusme_tarihi,
        data.menti_ad_soyad,
        data.mentor_ad_soyad,
        data.it_sektor_bilgisi,
        data.vit_katilim_uygun,
        data.mentor_degerlendirme,
        data.katilimci_yogunluk,
        data.yorumlar 
    ]

    add_mentor(sheet_id, row)

    return {"status": "ok"}
