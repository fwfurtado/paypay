from typing import Optional, Dict

from src.paypay.models.user import User


class UserRepository:
    IDENTITY: int = 0
    DB: Dict[int, User] = dict()

    def save(self, user: User):
        UserRepository.IDENTITY += 1

        user.id = UserRepository.IDENTITY

        UserRepository.DB[UserRepository.IDENTITY] = user

    def find_by_username(self, username: str) -> Optional[User]:
        result = [
            user for user in UserRepository.DB.values() if user.username == username
        ]

        if result:
            return result[0]

        return None

    def find_by_token(self, token: str) -> Optional[User]:
        result = [user for user in UserRepository.DB.values() if user.token == token]

        if result:
            return result[0]

        return None
