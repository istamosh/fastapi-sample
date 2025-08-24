from app.core.database import SQLModel
from sqlmodel import Field, Column, String
from typing import Optional
from enum import Enum
from datetime import datetime, UTC

class Role(str, Enum):
    player = "player"
    developer = "developer"

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    # property stays at password for ORM operation, but column/field name in db is hashed_password
    password: str = Field(sa_column=Column("hashed_password", String))
    role: Role
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))