from fastapi import APIRouter
import os
from dotenv import load_dotenv

from schemas.mentors import MentorCreate
from services.mentors_service import list_mentors, create_mentor

load_dotenv()
SHEET_ID = os.getenv("MENTOR_SHEET_ID")

router = APIRouter(prefix="/mentors", tags=["mentors"])

@router.get("")
def get_mentors():
    return list_mentors(SHEET_ID)

@router.post("")
def post_mentor(data: MentorCreate):
    return create_mentor(SHEET_ID, data)
