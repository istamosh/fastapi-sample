from fastapi import APIRouter

authRouter = APIRouter()

@authRouter.post("/login")
async def login():
    return {}

@authRouter.post("/signup")
async def signup():
    return {}

@authRouter.get("/refresh-token")
async def refresh_token():
    return {}