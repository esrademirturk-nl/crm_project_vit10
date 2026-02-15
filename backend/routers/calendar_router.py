from fastapi import APIRouter
from typing import List
from backend.services.calendar_service import list_events
from backend.schemas.calendar import CalendarEvent

router = APIRouter()

@router.get("/calendar/events", response_model=List[CalendarEvent])
def get_events():
    return list_events()
