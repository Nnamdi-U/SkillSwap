from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.notifications import router as notifications_router
from app.core.config import settings
from app.db.session import Base, engine
from app import models

app = FastAPI(title=settings.service_name)
app.include_router(health_router)
app.include_router(notifications_router)


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
