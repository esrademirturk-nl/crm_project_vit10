from pydantic import BaseModel
from typing import List, Optional

class CalendarEvent(BaseModel):
    event_name: Optional[str]
    event_time: Optional[str]
    participant_emails: List[str]
    organizer_email: Optional[str]
