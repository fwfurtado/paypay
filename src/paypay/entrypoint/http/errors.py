from typing import Dict, Type

from fastapi import status
from src.paypay.exeptions.payment import NewlyCreatedPayment, PaymentNotFound
from src.paypay.exeptions.user import (
    UserAlreadyExist,
    InvalidToken,
    InvalidUsernamePassword,
)

HTTP_ERRORS: Dict[Type[Exception], int] = {
    UserAlreadyExist: status.HTTP_409_CONFLICT,
    PaymentNotFound: status.HTTP_404_NOT_FOUND,
    NewlyCreatedPayment: status.HTTP_409_CONFLICT,
    InvalidToken: status.HTTP_401_UNAUTHORIZED,
    InvalidUsernamePassword: status.HTTP_401_UNAUTHORIZED,
}
