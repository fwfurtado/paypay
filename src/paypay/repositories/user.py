from typing import Optional
from sqlalchemy.orm import Session
from src.paypay.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.__session = session

    def save(self, user: User):
        if not user.id:
            self.__session.add(user)
        else:
            self.__session.merge(user)

    def find_by_username(self, username: str) -> Optional[User]:
        return self.__session.query(User).filter(User.username == username).first()

    def find_by_token(self, token: str) -> Optional[User]:
        return self.__session.query(User).filter(User.token == token).first()
