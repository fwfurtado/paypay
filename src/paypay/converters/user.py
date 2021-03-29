from src.paypay.forms.user import UserForm
from src.paypay.models.user import User


class UserFormToUser:
    def convert(self, form: UserForm, hashed_password: str) -> User:
        return User(username=form.username, password=hashed_password)
