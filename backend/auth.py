# backend/auth.py
from __future__ import annotations

from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Proje: Sheets + Calendar + Gmail
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]

BASE_DIR = Path(__file__).resolve().parent              # .../backend
TOKEN_PATH = BASE_DIR / "token.json"                   # .../backend/token.json
CREDS_PATH = BASE_DIR / "credentials.json"             # .../backend/credentials.json


def auth() -> Credentials:
    creds: Credentials | None = None

    # 1) token varsa yükle
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    # 2) token yoksa / geçersizse düzelt
    if not creds or not creds.valid:
        # Süresi dolduysa sessiz refresh (login açmaz)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # İlk defa veya refresh token yoksa: 1 kez login açar
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_PATH), SCOPES)
            creds = flow.run_local_server(port=0)

        # 3) token'ı kaydet
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")

    return creds
