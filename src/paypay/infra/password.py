from argon2 import PasswordHasher
from typing import Protocol
from src.paypay.models.user import User

class HasherProtocol(Protocol):
    def hash(self, password: str) -> str:
        ...
    def verify(self, hash: str, password: str) -> bool:
        ...

class PasswordService:

    def __init__(self, hasher: HasherProtocol):
        self.__hasher = hasher

    def verify(self, user: User, password: str) -> bool:
        return self.__hasher.verify(user.password, password)

    def encode(self, password: str) -> str:
        return self.__hasher.hash(password=password)