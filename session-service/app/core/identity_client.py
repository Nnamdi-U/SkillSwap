import httpx
from fastapi import HTTPException, status

from app.core.config import settings

REQUEST_ID_HEADER = "X-Request-ID"


def validate_profile_exists(profile_id: int, request_id: str, profile_label: str):
    headers = {REQUEST_ID_HEADER: request_id}
    profile_url = f"{settings.identity_service_url}/api/v1/profiles/{profile_id}"

    try:
        response = httpx.get(profile_url, headers=headers, timeout=5.0)
    except httpx.RequestError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Identity service is unavailable",
        )

    if response.status_code == status.HTTP_404_NOT_FOUND:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{profile_label} profile does not exist",
        )
    if response.status_code >= 400:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Identity service returned an error",
        )

    return response.json()
