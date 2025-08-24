from pydantic import BaseModel
from typing import Optional, Union
from app.db.models.user import Role
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    role: Role

class UserRead(BaseModel):
    id: int
    username: str
    role: Role
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    id: int
    username: Union[str, None] = None
    password: Union[str, None] = None

class UserLogin(BaseModel):
    username: str
    password: str

class UserWithToken(BaseModel):
    token: str