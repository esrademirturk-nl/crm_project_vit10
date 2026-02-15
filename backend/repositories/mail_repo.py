import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from backend.auth import auth

def send_gmail(to_email: str, subject: str, body: str):
    creds = auth()
    service = build("gmail", "v1", credentials=creds)

    message = MIMEText(body, "plain", "utf-8")
    message["to"] = to_email
    message["subject"] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

    service.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()
