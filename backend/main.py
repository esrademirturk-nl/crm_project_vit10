
from fastapi import FastAPI
from routers.users_router import router as users_router
from routers.applications_router import router as applications_router
from routers.mentors_router import router as mentors_router
from routers.interviews_router import router as interviews_router

app = FastAPI(title="CRM API (Sheets DB)")
app.include_router(users_router)
app.include_router(applications_router)
app.include_router(mentors_router)
app.include_router(interviews_router)


@app.get("/")
def root():
    return {"status": "ok"}
