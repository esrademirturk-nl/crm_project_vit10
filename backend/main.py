
from fastapi import FastAPI
from backend.routers.users_router import router as users_router
from backend.routers.applications_router import router as applications_router
from backend.routers.mentors_router import router as mentors_router
from backend.routers.interviews_router import router as interviews_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CRM API (Sheets DB)")
app.include_router(users_router)
app.include_router(applications_router)
app.include_router(mentors_router)
app.include_router(interviews_router)
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

@app.get("/")
def root():
    return {"status": "ok"}
