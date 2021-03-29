from src.paypay.converters.user import UserFormToUser
from src.paypay.exeptions.user import  UserAlreadyExist
from src.paypay.forms.user import UserForm
from src.paypay.repositories.user import  UserRepository
from src.paypay.models.user import User

class UserController:

    def __init__(self, userform_converter: UserFormToUser, user_repository: UserRepository):
        self.__userform_converter = userform_converter
        self.__user_repository = user_repository

    def register(self, form: UserForm) -> User:

        if self.__user_repository.find_by_username(form.username):
            raise UserAlreadyExist(f"User {form.username} already exist")

        user = self.__userform_converter.convert(form)
        self.__user_repository.save(user)

        return user



