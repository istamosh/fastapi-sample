from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.schemas.user import UserLogin, UserCreate
from app.core.dependencies import get_session
from app.service.user import UserService, UserWithToken, UserRead

authRouter = APIRouter()

@authRouter.post("/login", 
                 status_code=200, 
                 response_model=UserWithToken,
                 responses={
                     401: {"description": "Unauthorized. Invalid credentials."},
                 }
                 )
async def login(loginDetails: UserLogin, session: Session = Depends(get_session)):
    try:
        return UserService(session=session).login(login_details=loginDetails)
    except Exception as error:
        print(error)
        raise error

@authRouter.post("/signup",
                 status_code=201,
                 response_model=UserRead
                 )
async def signup(signupDeails: UserCreate, session: Session = Depends(get_session)):
    try: 
        return UserService(session=session).signup(user_details=signupDeails)
    except Exception as error:
        print(error)
        raise error

@authRouter.get("/refresh-token")
async def refresh_token():
    return {}