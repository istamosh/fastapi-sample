from fastapi import APIRouter
from app.db.schemas.user import UserLogin, UserCreate
from app.core.database import SessionDep
from app.service.user import UserService, UserWithToken, UserRead

authRouter = APIRouter()

@authRouter.post("/login", 
                 status_code=200, 
                 response_model=UserWithToken
                 )
async def login(loginDetails: UserLogin, session: SessionDep):
    try:
        return UserService(session=session).login(login_details=loginDetails)
    except Exception as error:
        print(error)
        raise error

@authRouter.post("/signup",
                 status_code=200,
                 response_model=UserRead
                 )
async def signup(signupDeails: UserCreate, session: SessionDep):
    try: 
        return UserService(session=session).signup(user_details=signupDeails)
    except Exception as error:
        print(error)
        raise error

@authRouter.get("/refresh-token")
async def refresh_token():
    return {}