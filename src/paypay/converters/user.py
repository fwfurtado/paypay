from src.paypay.forms.user import UserForm
from src.paypay.models.user import User

class UserFormToUser:


    def convert(self, form: UserForm) -> User:
        return  User(username=form.username, password=form.password)