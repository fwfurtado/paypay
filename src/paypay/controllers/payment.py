from asyncio import sleep

from src.paypay.forms.payment import CreationPaymentForm
from src.paypay.converters.payment import CreationPaymentToPayment
from src.paypay.models.payment import Payment
from src.paypay.repositories.payment import PaymentRepository
from src.paypay.exeptions.payment import NewlyCreatedPayment


class PaymentController:
    def __init__(
        self,
        creation_payment_converter: CreationPaymentToPayment,
        repository: PaymentRepository,
    ):
        self.__creation_payment_converter = creation_payment_converter
        self.__repository = repository

    async def pay(self, form: CreationPaymentForm) -> Payment:
        payment = self.__creation_payment_converter.convert(form=form)

        if self.__repository.anyone_is_same(payment=payment):
            raise NewlyCreatedPayment(
                "There is a payment with same information created a few minutes ago"
            )

        await sleep(3)

        payment.confirm()

        self.__repository.save(payment=payment)

        return payment
