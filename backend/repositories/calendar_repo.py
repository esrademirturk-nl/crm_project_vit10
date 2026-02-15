from googleapiclient.discovery import build
from backend.auth import auth

def get_calendar_events(calendar_id="primary", max_results=20):
    creds = auth()
    service = build("calendar", "v3", credentials=creds)

    result = service.events().list(
        calendarId=calendar_id,
        maxResults=max_results,
        singleEvents=True,
        orderBy="startTime",
    ).execute()

    return result.get("items", [])
