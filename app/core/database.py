from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager

# from app.db.models.firearm import Hero

# class Hero(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     age: int | None = Field(default=None, index=True)
#     secret_name: str


# sqlite_file_name = "database.db"

# postgresql:// -> connect to postgresql url format
# user:postgres -> the username with password separated by colon
# @db:5432 -> connect to db service (db on docker compose) on port 5432, not localhost:5432
# /fastapi_sample_db -> the db name
DB_URL = "postgresql://user:postgres@db:5432/fastapi_sample_db"

# check same thread will return error using psycopg2
# connect_args = {"check_same_thread": False}
# engine = create_engine(DB_URL, connect_args=connect_args)
engine = create_engine(DB_URL)

# engine creation before importing deps
from app.core.dependencies import get_session

from app.routes.user import userRouter
from app.routes.auth import authRouter

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

SessionDep = Annotated[Session, Depends(get_session)]

# create tables on startup
# -- DEPRECATED -- #
# app = FastAPI()

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

# -- NEWEST -- #
@asynccontextmanager
async def lifespan(app: FastAPI):
    # run on startup
    print("Starting up: creating database tables...")
    create_db_and_tables()
    yield
    # on shutdown
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(userRouter, tags=["User"])
app.include_router(authRouter, tags=["Auth"], prefix="/auth")

# @app.get("/health/")
# async def health_check():
#     return {"status": "healthy"}

# @app.post("/heroes/")
# async def create_hero(hero: Hero, session: SessionDep) -> Hero:
#     session.add(hero)
#     session.commit()
#     session.refresh(hero)
#     return hero


# @app.get("/heroes/")
# async def read_heroes(
#     session: SessionDep,
#     offset: int = 0,
#     limit: Annotated[int, Query(le=100)] = 100,
# ) -> list[Hero]:
#     heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
#     return heroes


# @app.get("/heroes/{hero_id}")
# async def read_hero(hero_id: int, session: SessionDep) -> Hero:
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     return hero


# @app.delete("/heroes/{hero_id}")
# async def delete_hero(hero_id: int, session: SessionDep):
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     session.delete(hero)
#     session.commit()
#     return {"ok": True}