from fastapi import APIRouter
import os
from dotenv import load_dotenv
from backend.schemas.interviews import InterviewCreate
from backend.services.interviews_service import list_interviews, create_interview

load_dotenv()
SHEET_ID = os.getenv("INTERVIEWS_SHEET_ID")

router = APIRouter(prefix="/interviews", tags=["interviews"])

@router.get("")
def get_interviews():
    return list_interviews(SHEET_ID)

@router.post("")
def post_interview(data: InterviewCreate):
    return create_interview(SHEET_ID, data)



