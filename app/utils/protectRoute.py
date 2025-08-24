from fastapi import Depends, Header, HTTPException, status, Security
from sqlmodel import Session
from typing import Annotated, Union
from app.core.dependencies import get_session
from app.core.security.authHandler import AuthHandler
from app.service.user import UserRead, UserService, UserRepository
from fastapi.security import HTTPAuthorizationCredentials
from app.core.security.httpBearer import security

BEARER = 'Bearer '

def get_current_user(
        session: Session = Depends(get_session),
        credentials: HTTPAuthorizationCredentials = Security(security)
) -> UserRead:
    auth_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail= "Invalid authentication credentials.",
        headers={"WWW-Authenticate": "Bearer"}
    )

    # print(credentials.credentials)

    # if not authorization or not authorization.startswith(BEARER):
    #     raise auth_exception
    
    payload = AuthHandler.decode_jwt(
        token=credentials.credentials
    )

    if payload and payload["user_id"]:
        try:
            # passing UserRepository directly instead of by UserService first
            user = UserRepository(session=session).get_user_by_id(payload["user_id"])
            return UserRead(
                id=user.id,
                username=user.username,
                role=user.role,
                created_at=user.created_at,
                updated_at=user.updated_at
            )
        except Exception as error:
            raise error
    raise auth_exception