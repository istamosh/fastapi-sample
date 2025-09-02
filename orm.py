from sqlmodel import Session, SQLModel, Field, create_engine, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True)
    password: str

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