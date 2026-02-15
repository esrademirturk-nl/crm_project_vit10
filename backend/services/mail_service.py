from backend.repositories.mail_repo import send_gmail

def send_mail_service(to_email: str, subject: str, body: str):
    send_gmail(to_email, subject, body)
    return {"status": "success", "to": to_email}
