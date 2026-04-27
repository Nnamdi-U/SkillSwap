from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.db.session import Base


class SkillSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    requester_profile_id = Column(Integer, index=True, nullable=False)
    mentor_profile_id = Column(Integer, index=True, nullable=False)
    requested_skill = Column(String(120), nullable=False)
    message = Column(Text, nullable=True)
    scheduled_date = Column(DateTime, nullable=True)
    status = Column(String(30), default="requested", index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
