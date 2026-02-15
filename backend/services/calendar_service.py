from backend.repositories.calendar_repo import get_calendar_events

def list_events():
    events = get_calendar_events()
    formatted = []

    for ev in events:
        formatted.append({
            "event_name": ev.get("summary"),
            "event_time": ev.get("start", {}).get("dateTime") 
                          or ev.get("start", {}).get("date"),
            "participant_emails": [
                a.get("email")
                for a in (ev.get("attendees") or [])
                if a.get("email")
            ],
            "organizer_email": ev.get("organizer", {}).get("email")
        })

    return formatted
