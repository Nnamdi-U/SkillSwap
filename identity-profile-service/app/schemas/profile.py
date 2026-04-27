from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProfileCreate(BaseModel):
    user_id: int
    full_name: str
    bio: str | None = None
    city: str | None = None
    can_teach: str | None = None
    wants_to_learn: str | None = None


class ProfileRead(ProfileCreate):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
