from fastapi import APIRouter
import os
from dotenv import load_dotenv
from schemas.applications import ApplicationCreate
from services.applications_service import list_applications, create_application

load_dotenv()
SHEET_ID = os.getenv("APPLICATIONS_SHEET_ID")

router = APIRouter(prefix="/applications", tags=["applications"])

@router.get("")
def get_applications():
    return list_applications(SHEET_ID)

@router.post("")
def post_application(data: ApplicationCreate):
    return create_application(SHEET_ID, data)
