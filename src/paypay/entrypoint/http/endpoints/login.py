from dataclasses import dataclass

from argon2 import PasswordHasher
from fastapi import APIRouter, Depends
from fastapi.security import  OAuth2PasswordRequestForm

from src.paypay.controllers.user import UserController
from src.paypay.entrypoint.http.dependencies.user import user_controller

router = APIRouter()

@dataclass()
class AccessToken():
    access_token: str
    token_type: str = "bearer"


@router.post("/oauth/token")
async def login(
        form: OAuth2PasswordRequestForm = Depends(),
        controller: UserController = Depends(user_controller),
) -> AccessToken:
    user = controller.login(form.username, form.password)

    return AccessToken(access_token=user.token)