from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.session import SkillSession
from app.schemas.session import SkillSessionCreate, SkillSessionRead

router = APIRouter(prefix="/api/v1/sessions", tags=["sessions"])


@router.post("", response_model=SkillSessionRead, status_code=201)
def create_session(session: SkillSessionCreate, db: Session = Depends(get_db)):
    db_session = SkillSession(**session.model_dump())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


@router.get("", response_model=list[SkillSessionRead])
def list_sessions(status: str | None = None, db: Session = Depends(get_db)):
    query = db.query(SkillSession)
    if status:
        query = query.filter(SkillSession.status == status)
    return query.all()
