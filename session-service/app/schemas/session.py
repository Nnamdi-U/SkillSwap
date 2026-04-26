from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SkillSessionCreate(BaseModel):
    requester_profile_id: int
    mentor_profile_id: int
    requested_skill: str
    message: str | None = None
    scheduled_date: datetime | None = None


class SkillSessionRead(SkillSessionCreate):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
