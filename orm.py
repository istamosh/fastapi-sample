from sqlmodel import Session, SQLModel, Field, create_engine, select, Relationship
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.exc import IntegrityError

# model section
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True)
    password: str

class Caliber(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    # relationship back to firearm
    firearms: List["Firearm"] = Relationship(back_populates="caliber")

class Firearm(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    barrel_count: int = Field(default=1)
    operation: str
    caliber_id: int = Field(foreign_key="caliber.id")
    # relationship
    caliber: Optional[Caliber] = Relationship(back_populates="firearms")

# schema section
class FirearmCreate(SQLModel):
    name: str
    caliber: str
    barrel_count: Optional[int] = 1
    operation: str

class CaliberCreate(SQLModel):
    name: str

user1 = User(username="johndoe", email="johndoe@test.com", password="test123")
admin1 = User(username="admin", email="admin@test.com", password="admin123")

DB_URL = "postgresql://user:postgres@db:5432/fastapi_sample_db"

engine = create_engine(DB_URL,
                       echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def seed_users():
    with Session(engine) as session:
        session.add(user1)
        session.add(admin1)

        session.commit()

# helper function
def register_firearm(firearm: FirearmCreate) -> Firearm:
    # check if caliber is already exists
    with Session(engine) as session:
        # try to create caliber first
        try:
            caliber = Caliber(name=firearm.caliber)
            session.add(caliber)
            session.flush() # flush to get id without commit
        except IntegrityError:
            # caliber already exists
            session.rollback()
            statement = select(Caliber).where(Caliber.name == firearm.caliber)
            caliber = session.exec(statement).first()

            if not caliber:
                raise ValueError(f"Caliber {firearm.caliber} not found after integrity error")

        # create the firearm
        if "barrel_count" in firearm:
            firearm_entry = Firearm(
                name=firearm.name,
                caliber_id=caliber.id,
                operation=firearm.operation,
                barrel_count=firearm.barrel_count
            )
        else:
            firearm_entry = Firearm(
                name=firearm.name,
                caliber_id=caliber.id,
                operation=firearm.operation,
            )

        session.add(firearm_entry)
        session.commit()
        session.refresh(firearm_entry)
        return firearm_entry

# test the query and print
# with Session(engine) as session:
#     statement = select(User).where(User.email == "johndoe@test.com")
#     user = session.exec(statement).first()
#     print(user)

def main():
    create_db_and_tables()
    seed_users()

# if __name__ == "__main__":
#     main()