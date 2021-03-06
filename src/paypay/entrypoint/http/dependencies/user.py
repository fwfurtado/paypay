from fastapi import Depends
from sqlalchemy.orm import Session

from src.paypay.controllers.user import UserController
from src.paypay.converters.user import UserFormToUser
from src.paypay.entrypoint.http.dependencies.commons import (
    oauth_scheme,
    password_service,
    token_service,
    session_factory,
)
from src.paypay.exeptions.user import InvalidToken
from src.paypay.infra.password import PasswordService
from src.paypay.infra.token import TokenService
from src.paypay.models.user import User
from src.paypay.repositories.user import UserRepository


async def user_repository(
    session: Session = Depends(session_factory),
) -> UserRepository:
    return UserRepository(session=session)


async def userform_to_user() -> UserFormToUser:
    return UserFormToUser()


async def user_controller(
    converter: UserFormToUser = Depends(userform_to_user),
    repository: UserRepository = Depends(user_repository),
    password_service: PasswordService = Depends(password_service),
    token_service: TokenService = Depends(token_service),
) -> UserController:
    return UserController(
        userform_converter=converter,
        user_repository=repository,
        password_service=password_service,
        token_service=token_service,
    )


async def load_user(
    repository: UserRepository = Depends(user_repository),
    token: str = Depends(oauth_scheme),
) -> User:
    user = repository.find_by_token(token=token)

    if not user:
        raise InvalidToken("Invalid token")

    return user
