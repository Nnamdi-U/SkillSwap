import json
import logging
import time
from uuid import uuid4

from fastapi import FastAPI, Request

from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.mfa import router as mfa_router
from app.api.profiles import router as profiles_router
from app.core.config import settings
from app.db.session import Base, engine
from app import models

REQUEST_ID_HEADER = "X-Request-ID"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(settings.service_name)

app = FastAPI(title=settings.service_name)


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get(REQUEST_ID_HEADER) or str(uuid4())
    request.state.request_id = request_id
    started_at = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        duration_ms = round((time.perf_counter() - started_at) * 1000, 2)
        logger.exception(
            json.dumps(
                {
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "status_code": 500,
                    "duration_ms": duration_ms,
                }
            )
        )
        raise

    duration_ms = round((time.perf_counter() - started_at) * 1000, 2)
    response.headers[REQUEST_ID_HEADER] = request_id
    logger.info(
        json.dumps(
            {
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
            }
        )
    )
    return response


app.include_router(auth_router)
app.include_router(health_router)
app.include_router(mfa_router)
app.include_router(profiles_router)


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
