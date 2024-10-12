from typing import Optional
from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoResponse(TodoCreate):
    id: int

    class Config:
        orm_mode = True