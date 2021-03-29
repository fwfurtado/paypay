from fastapi import APIRouter, Depends
from src.paypay.controllers.user import UserController
from src.paypay.entrypoint.http.dependencies.user import user_controller
from src.paypay.forms.user import UserForm
from src.paypay.models.user import User

router = APIRouter(prefix="/users")


@router.post("/", status_code=201)
def create_user(form: UserForm, controller: UserController = Depends(user_controller)) -> User:
    return controller.register(form=form)
