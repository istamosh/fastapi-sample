from app.core.database import SQLModel
from sqlmodel import Field, Column, String, Relationship
from typing import Optional
from enum import Enum
from datetime import datetime, UTC
from .caliber import Caliber

class Cartridge(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    caliber_id: Optional[int] = Field(default=None, foreign_key="caliber.id")
    caliber: Caliber = Relationship(back_populates="cartridges")
