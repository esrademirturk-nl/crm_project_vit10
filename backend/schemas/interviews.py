from pydantic import BaseModel

class InterviewCreate(BaseModel):
    ad_soyad: str
    proje_gonderilis_tarihi: str
    projenin_gelis_tarihi: str
