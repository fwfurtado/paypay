from fastapi import Depends
from src.paypay.controllers.user import UserController
from src.paypay.converters.user import UserFormToUser
from src.paypay.repositories.user import UserRepository


async def user_repository() -> UserRepository:
    return UserRepository()


async def userform_to_user() -> UserFormToUser:
    return UserFormToUser()


async def user_controller(
    converter: UserFormToUser = Depends(userform_to_user),
    repository: UserRepository = Depends(user_repository),
) -> UserController:
    return UserController(userform_converter=converter, user_repository=repository)
