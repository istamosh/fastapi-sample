from fastapi import APIRouter, FastAPI, Depends, Request
from app.db.schemas.user import UserRead
from app.utils.protectRoute import get_current_user

# app = FastAPI()
userRouter = APIRouter()


@userRouter.get("/users")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


# app.include_router(router)

# test protected route
@userRouter.get("/me")
async def read_profile(user: UserRead = Depends(get_current_user)):
    return {"data" : user}