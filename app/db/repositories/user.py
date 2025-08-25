from .base import BaseRepository
from app.db.models.user import User
from app.db.schemas.user import UserCreate
from sqlmodel import select
from datetime import datetime, UTC

class UserRepository(BaseRepository):
    def create_user(self, user_data: UserCreate):
        # adding several params arbitrarily
        newUser = User(**user_data.model_dump(exclude_none=True))

        self.session.add(instance=newUser)
        self.session.commit()
        self.session.refresh(instance=newUser)

        return newUser
    
    def is_user_exists(self, username: str) -> bool:
        # communicate with db just like mysql query
        statement = select(User).where(User.username == username)
        user = self.session.exec(statement).first()
        return bool(user)
    
    def get_user(self, username: str) -> User:
        statement = select(User).where(User.username == username)
        user = self.session.exec(statement).first()
        return user
    
    def get_user_by_id(self, user_id: int) -> User:
        statement = select(User).where(User.id == user_id)
        user = self.session.exec(statement).first()
        return user
    
    def update_user(self, user_id: int, update_payload: dict):
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        # update the user data using the payload from the service layer
        for key, value in update_payload.items():
            setattr(user, key, value)

        # don't forget to alter the time
        user.updated_at = datetime.now(UTC)

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user