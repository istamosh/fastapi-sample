from fastapi import APIRouter, FastAPI, Depends, Request
from sqlmodel import Session
from app.core.dependencies import get_session
from app.db.schemas.user import UserRead, UserUpdate as UserUpdateSchema
from app.utils.protectRoute import get_current_user
from app.service.user import UserService

# app = FastAPI()
userRouter = APIRouter()


@userRouter.get("/users")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


# app.include_router(router)

# test protected route
@userRouter.get("/me")
async def read_profile(user: UserRead = Depends(get_current_user)):
    return {"data": user}

@userRouter.put("/me", response_model=UserRead)
async def update_profile(
    update_details: UserUpdateSchema,
    user: UserRead = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    return UserService(session=session).update_profile(
        user_id=user.id, update_details=update_details
        )