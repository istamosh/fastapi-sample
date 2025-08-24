from app.db.repositories.user import UserRepository
from app.db.schemas.user import *
from app.core.security import hashHelper, authHandler
from sqlmodel import Session
from fastapi import HTTPException

class UserService:
    def __init__(self, session: Session):
        self.__userRepository = UserRepository(session=session)
        
    def signup(self, user_details: UserCreate) -> UserRead:
        if self.__userRepository.is_user_exists(username=user_details.username):
            raise HTTPException(status_code=400, detail="Please login")
        
        hashed_password = hashHelper.HashHelper.get_password_hash(plain_password=user_details.password)

        # convert the plain password into the hashed one
        user_details.password = hashed_password

        return self.__userRepository.create_user(user_data=user_details)
    
    def login(self, login_details: UserLogin) -> UserWithToken:
        user = self.__userRepository.get_user(username=login_details.username)

        # check if user is nonexistent
        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized. Invalid credentials.")

        # using user.hashed_password rather than user.password
        if hashHelper.HashHelper.verify_password(plain_password=login_details.password, hashed_password=user.password):
            token = authHandler.AuthHandler.sign_jwt(user_id=user.id)

            if token:
                return UserWithToken(token=token)
            raise HTTPException(status_code=500, detail="Unable to process request")
        raise HTTPException(status_code=401, detail="Unauthorized. Invalid credentials.")