from argon2 import PasswordHasher  # type: ignore
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from paypay.infra.database import SessionLocal # type: ignore
from src.paypay.infra.password import PasswordService
from src.paypay.infra.token import TokenService

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/oauth/token")


async def password_service() -> PasswordService:
    return PasswordService(hasher=PasswordHasher())


async def token_service() -> TokenService:
    return TokenService()


def session_factory() -> Session: # type: ignore
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:  # noqa: E722
        session.rollback()
