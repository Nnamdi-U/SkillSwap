from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.profiles import router as profiles_router
from app.core.config import settings
from app.db.session import Base, engine
from app import models

app = FastAPI(title=settings.service_name)
app.include_router(auth_router)
app.include_router(health_router)
app.include_router(profiles_router)


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
