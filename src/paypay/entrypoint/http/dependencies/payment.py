from fastapi import Depends
from sqlalchemy.orm import Session

from src.paypay.entrypoint.http.dependencies.commons import session_factory
from src.paypay.controllers.payment import PaymentController
from src.paypay.converters.payment import CreationPaymentToPayment
from src.paypay.repositories.payment import PaymentRepository


async def creation_payment_converter() -> CreationPaymentToPayment:
    return CreationPaymentToPayment()


async def payment_repository(session: Session = Depends(session_factory)) -> PaymentRepository:
    return PaymentRepository(session=session)


async def payment_controller(
    converter: CreationPaymentToPayment = Depends(creation_payment_converter),
    repository: PaymentRepository = Depends(payment_repository),
) -> PaymentController:
    return PaymentController(
        creation_payment_converter=converter, repository=repository
    )
