from argon2 import PasswordHasher
from fastapi.security import OAuth2PasswordBearer
from src.paypay.infra.password import PasswordService
from src.paypay.infra.token import TokenService

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/oauth/token")


async def password_service() -> PasswordService:
    return PasswordService(hasher=PasswordHasher())

async def token_service() -> TokenService:
    return TokenService()