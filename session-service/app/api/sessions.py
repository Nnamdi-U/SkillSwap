from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.identity_client import validate_profile_exists
from app.core.notification_client import create_session_request_notification
from app.db.session import get_db
from app.models.session import SkillSession
from app.schemas.session import SkillSessionCreate, SkillSessionRead

router = APIRouter(prefix="/api/v1/sessions", tags=["sessions"])


@router.post("", response_model=SkillSessionRead, status_code=201)
def create_session(session: SkillSessionCreate, request: Request, db: Session = Depends(get_db)):
    request_id = request.state.request_id
    validate_profile_exists(session.requester_profile_id, request_id, "Requester")
    validate_profile_exists(session.mentor_profile_id, request_id, "Mentor")

    db_session = SkillSession(**session.model_dump())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)

    create_session_request_notification(
        profile_id=db_session.mentor_profile_id,
        session_id=db_session.id,
        request_id=request_id,
    )
    return db_session


@router.get("", response_model=list[SkillSessionRead])
def list_sessions(status: str | None = None, db: Session = Depends(get_db)):
    query = db.query(SkillSession)
    if status:
        query = query.filter(SkillSession.status == status)
    return query.all()
