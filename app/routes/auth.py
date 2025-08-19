from fastapi import APIRouter
from app.db.schemas.user import UserLogin, UserCreate

authRouter = APIRouter()

@authRouter.post("/login")
async def login(loginDetails: UserLogin):
    return {"data": loginDetails}

@authRouter.post("/signup")
async def signup(signupDeails: UserCreate):
    return {"data": signupDeails}

@authRouter.get("/refresh-token")
async def refresh_token():
    return {}