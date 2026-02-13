from fastapi import APIRouter, HTTPException,Query
import os
from dotenv import load_dotenv
from backend.schemas.applications import ApplicationCreate
from backend.services.applications_service import list_applications, create_application

load_dotenv()
SHEET_ID = (os.getenv("APPLICATIONS_SHEET_ID") or "").strip()

router = APIRouter(prefix="/applications", tags=["applications"])

@router.get("")
def get_applications(tab: str = Query("all", enum=["all", "vit1", "vit2"])):
    if not SHEET_ID:
        raise HTTPException(status_code=500, detail="APPLICATIONS_SHEET_ID missing")

    try:
        return list_applications(SHEET_ID, tab_key=tab)
    except Exception as e:
        # Swagger’da gerçek hatayı gör
        raise HTTPException(status_code=500, detail=str(e))


    
@router.post("")
def post_application(data: ApplicationCreate):
    if not SHEET_ID:
        raise HTTPException(status_code=500, detail="APPLICATIONS_SHEET_ID is missing. Check your .env file location/content.")
    return create_application(SHEET_ID, data)
