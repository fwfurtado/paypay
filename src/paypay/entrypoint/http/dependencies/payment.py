from fastapi import Depends

from src.paypay.controllers.payment import PaymentController
from src.paypay.converters.payment import CreationPaymentToPayment
from src.paypay.repositories.payment import PaymentRepository


async def creation_payment_converter() -> CreationPaymentToPayment:
    return CreationPaymentToPayment()


async def payment_repository() -> PaymentRepository:
    return PaymentRepository()


async def payment_controller(
    converter: CreationPaymentToPayment = Depends(creation_payment_converter),
    repository: PaymentRepository = Depends(payment_repository),
) -> PaymentController:
    return PaymentController(
        creation_payment_converter=converter, repository=repository
    )
