from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"service": "identity-profile-service", "status": "ok"}
