from fastapi import APIRouter
from backend.schemas.mail import MailRequest
from backend.services.mail_service import send_mail_service

router = APIRouter()

@router.post("/mail/send")
def send_mail(mail: MailRequest):
    return send_mail_service(mail.to_email, mail.subject, mail.body)
