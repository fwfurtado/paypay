from fastapi import APIRouter
from paypay.forms.user import UserForm

router = APIRouter(prefix="/users")


@router.post("/", status_code=201)
def create_user(form: UserForm):
    return None
