from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager

from orm import main, FirearmCreate, register_firearm

# on_event is deprecated, use this instead
@asynccontextmanager
async def lifespan(app: FastAPI):
    main() # trigger the main function inside orm.py
    yield
    # cleanup

# pass lifespan to FastAPI
app = FastAPI(lifespan=lifespan)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def backend_health():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
def read_item(
    item_id: int,
    q: Union[str, None] = None
):
    return {
        "item_id" : item_id,
        "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_id": item_id
    }

@app.post("/firearm/")
def create_firearm(firearm: FirearmCreate):
    return register_firearm(firearm)