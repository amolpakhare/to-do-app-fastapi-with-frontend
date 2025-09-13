from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False


#for creation
class TodoCreate(TodoBase):
    pass


# for updation
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

#for response
class TodoInDBBase(TodoBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class Todo(TodoInDBBase):
    pass
