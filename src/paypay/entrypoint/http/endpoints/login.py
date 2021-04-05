from dataclasses import dataclass

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from src.paypay.controllers.user import UserController
from src.paypay.entrypoint.http.dependencies.user import user_controller
from src.paypay.exeptions.user import InvalidUsernamePassword, InvalidToken

router = APIRouter()


class AccessToken(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/oauth/token", response_model=AccessToken)
async def login(
    form: OAuth2PasswordRequestForm = Depends(),
    controller: UserController = Depends(user_controller),
) -> AccessToken:
    user = controller.login(form.username, form.password)

    if not user:
        raise InvalidUsernamePassword("Invalid username or password")

    if not user.token:
        raise InvalidToken("Invalid token")

    return AccessToken(access_token=user.token)
