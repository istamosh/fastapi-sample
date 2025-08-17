from typing import Union, Annotated
from fastapi import Query, HTTPException
from sqlmodel import select
from app.core.database import app, SessionDep
from app.db.models.firearm import Hero
# from fastapi import FastAPI

# app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "message": f"item id: {item_id}",
        "q": q
    }

@app.get("/health/")
async def health_check():
    return {"status": "healthy"}

@app.post("/heroes/")
async def create_hero(hero: Hero, session: SessionDep) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


@app.get("/heroes/")
async def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


@app.get("/heroes/{hero_id}")
async def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.delete("/heroes/{hero_id}")
async def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}

if __name__ == "__main__":
    read_root()