from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationRead

router = APIRouter(prefix="/api/v1/notifications", tags=["notifications"])


@router.post("", response_model=NotificationRead, status_code=201)
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    db_notification = Notification(**notification.model_dump())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


@router.get("", response_model=list[NotificationRead])
def list_notifications(db: Session = Depends(get_db)):
    return db.query(Notification).all()


@router.get("/profile/{profile_id}", response_model=list[NotificationRead])
def list_notifications_for_profile(profile_id: int, db: Session = Depends(get_db)):
    return db.query(Notification).filter(Notification.profile_id == profile_id).all()
