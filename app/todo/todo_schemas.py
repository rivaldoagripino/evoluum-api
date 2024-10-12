from pydantic import Field
from datetime import datetime

from app.middleware.evoluum_base_model import EvoluumBaseModel


class TodoCreate(EvoluumBaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1, max_length=1024)


class TodoResponse(EvoluumBaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
