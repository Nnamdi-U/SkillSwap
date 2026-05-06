import httpx
from fastapi import HTTPException, status

from app.core.config import settings

REQUEST_ID_HEADER = "X-Request-ID"


def create_session_request_notification(profile_id: int, session_id: int, request_id: str):
    headers = {REQUEST_ID_HEADER: request_id}
    notification_url = f"{settings.notification_service_url}/api/v1/notifications"
    payload = {
        "profile_id": profile_id,
        "type": "session_request",
        "message": f"You have a new session request #{session_id}.",
    }

    try:
        response = httpx.post(notification_url, json=payload, headers=headers, timeout=5.0)
    except httpx.RequestError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Notification service is unavailable",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Notification service returned an error",
        )

    return response.json()
