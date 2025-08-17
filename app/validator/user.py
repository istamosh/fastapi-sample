from pydantic import BaseModel
from typing import Optional
from app.db.models.user import Role

class UserCreate(BaseModel):
    username: str
    password: str # will be hashed in service layer
    role: Role

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[Role] = None