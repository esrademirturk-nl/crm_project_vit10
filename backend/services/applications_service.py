from repositories.applications_repo import list_applications_raw, add_application

def list_applications(sheet_id: str):
    values = list_applications_raw(sheet_id)
    if not values or len(values) == 1:
        return []

    header = values[0]
    rows = values[1:]

    result = []
    for r in rows:
        result.append(dict(zip(header, r)))
    return result

def create_application(sheet_id: str, data):
    row = [
        "",  # Zaman damgası (Sheets otomatik yazabilir)
        data.ad_soyad,
        data.email,
        data.telefon,
        data.posta_kodu,
        data.eyalet,
        data.mevcut_durum,
        data.katilim_itph,
        data.ekonomik_durum,
        data.dil_kursu,
        data.ingilizce_seviye,
        data.hollandaca_seviye,
        data.belediye_baski,
        data.baska_bootcamp,
        data.online_kurs,
        data.it_tecrube,
        data.aktif_proje,
        data.hedef_alanlar,
        data.vit_neden,
        data.motivasyon,
        data.mentor_gorusmesi or "",
        data.basvuru_donemi or "",
        data.yesil_tik or "",
    ]
    add_application(sheet_id, row)
    return {"status": "ok"}
