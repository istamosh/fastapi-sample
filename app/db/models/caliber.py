from app.core.database import SQLModel
from sqlmodel import Field, Column, String
from typing import Optional
from enum import Enum
from datetime import datetime, UTC

class Caliber(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

