from pydantic import BaseModel
from typing import Optional

class MentorCreate(BaseModel):
    gorusme_tarihi: str                 # "12.02.2026" gibi
    menti_ad_soyad: str
    mentor_ad_soyad: str
    it_sektor_bilgisi: str              # örn: "Temel / Orta / İleri"
    vit_katilim_uygun: str              # örn: "Uygun / Şartlı / Uygun değil"
    mentor_degerlendirme: str           # "Katılımcı hakkında ne düşünüyorsunuz"
    katilimci_yogunluk: str             # örn: "Çok yoğun / Uygun"
    yorumlar: Optional[str] = None      # "Katilimci hakkinda yorumlar"
