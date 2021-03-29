from src.paypay.converters.user import UserFormToUser
from src.paypay.exeptions.user import UserAlreadyExist, InvalidUsernamePassword
from src.paypay.forms.user import UserForm
from src.paypay.repositories.user import UserRepository
from src.paypay.models.user import User
from src.paypay.infra.password import PasswordService
from src.paypay.infra.token import TokenService


class UserController:
    def __init__(
        self,
        userform_converter: UserFormToUser,
        user_repository: UserRepository,
        password_service: PasswordService,
        token_service: TokenService,
    ):
        self.__userform_converter = userform_converter
        self.__user_repository = user_repository
        self.__password_service = password_service
        self.__token_service = token_service

    def register(self, form: UserForm) -> User:
        if self.__user_repository.find_by_username(form.username):
            raise UserAlreadyExist(f"User {form.username} already exist")

        password = self.__password_service.encode(form.password)
        user = self.__userform_converter.convert(form=form, hashed_password=password)
        self.__user_repository.save(user)

        return user

    def login(self, username: str, password: str) -> User:
        user = self.__user_repository.find_by_username(username=username)

        if not user:
            raise InvalidUsernamePassword("Invalid username or password")

        if not self.__password_service.verify(user, password):
            raise InvalidUsernamePassword("Invalid username or password")

        user.token = self.__token_service.generate_toke()

        self.__user_repository.save(user)

        return user
