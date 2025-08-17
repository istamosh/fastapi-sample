from fastapi import APIRouter, FastAPI

# app = FastAPI()
userRouter = APIRouter()


@userRouter.get("/users")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


# app.include_router(router)