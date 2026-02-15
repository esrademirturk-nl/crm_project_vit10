from pydantic import BaseModel

class MailRequest(BaseModel):
    to_email: str
    subject: str
    body: str
