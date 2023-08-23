from fastapi import FastAPI
from routes.user import user
from routes.patient import patient
from routes.schedule import schedule
from config.api import tags_metadata


app = FastAPI(
    title="Patients API with Fast ",
    description="REST API OFFICIAL",
    version="0.0.1",
    openapi_tags=tags_metadata,
)


app.include_router(user)
app.include_router(patient)
app.include_router(schedule)
