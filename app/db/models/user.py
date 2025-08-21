from app.core.database import SQLModel
from sqlmodel import Field
from typing import Optional
from enum import Enum
from datetime import datetime, UTC

class Role(str, Enum):
    player = "player"
    developer = "developer"

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    role: Role
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))