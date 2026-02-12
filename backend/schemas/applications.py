from pydantic import BaseModel
from typing import Optional

class ApplicationCreate(BaseModel):
    ad_soyad: str
    email: str
    telefon: str
    posta_kodu: str
    eyalet: str
    mevcut_durum: str
    katilim_itph: str
    ekonomik_durum: str
    dil_kursu: str
    ingilizce_seviye: str
    hollandaca_seviye: str
    belediye_baski: str
    baska_bootcamp: str
    online_kurs: str
    it_tecrube: str
    aktif_proje: str
    hedef_alanlar: str
    vit_neden: str
    motivasyon: str
    mentor_gorusmesi: Optional[str] = None
    basvuru_donemi: Optional[str] = None
    yesil_tik: Optional[str] = None
