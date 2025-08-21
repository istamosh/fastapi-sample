from sqlmodel import Session
from app.core.database import engine

# create session dependency
def get_session():
    with Session(engine) as session:
        yield session