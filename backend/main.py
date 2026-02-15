
from fastapi import FastAPI
from backend.routers.users_router import router as users_router
from backend.routers.applications_router import router as applications_router
from backend.routers.mentors_router import router as mentors_router
from backend.routers.interviews_router import router as interviews_router
from backend.routers.calendar_router import router as calendar_router
from backend.routers.mail_router import router as mail_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv



load_dotenv()
app = FastAPI(title="CRM API (Sheets DB)",debug=True)
app.include_router(users_router)
app.include_router(applications_router)
app.include_router(mentors_router)
app.include_router(interviews_router)
app.include_router(calendar_router)
app.include_router(mail_router)
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # geliştirme aşamasında ["*"] da yapabilirsin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/")
def root():
    return {"status": "ok"}
