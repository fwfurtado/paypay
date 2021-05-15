from typing import List

from asyncio import sleep

from src.paypay.forms.payment import CreationPaymentForm
from src.paypay.converters.payment import CreationPaymentToPayment
from src.paypay.models.payment import Payment
from src.paypay.models.user import User
from src.paypay.repositories.payment import PaymentRepository
from src.paypay.exeptions.payment import NewlyCreatedPayment, PaymentNotFound


class PaymentController:
    def __init__(
        self,
        creation_payment_converter: CreationPaymentToPayment,
        repository: PaymentRepository,
    ):
        self.__creation_payment_converter = creation_payment_converter
        self.__repository = repository

    def list_user_payments(self, user: User) -> List[Payment]:
        return self.__repository.find_all_by_user(owner_id=user.id)

    def __create_payment(self, form: CreationPaymentForm, user: User) -> Payment:
        payment = self.__creation_payment_converter.convert(form=form, user=user)

        if self.__repository.anyone_is_same(payment=payment):
            raise NewlyCreatedPayment(
                "There is a payment with same information created a few minutes ago"
            )

        return payment

    async def online_pay(self, form: CreationPaymentForm, user: User) -> Payment:
        payment = self.__create_payment(form=form, user=user)
        self.__repository.save(payment=payment)
        await sleep(3)

        payment.confirm()

        self.__repository.save(payment=payment)

        return payment

    async def bank_slip_pay(self, form: CreationPaymentForm, user: User) -> Payment:
        payment = self.__create_payment(form=form, user=user)

        self.__repository.save(payment=payment)

        return payment

    def __find_payment_by(self, payment_id: int, user: User) -> Payment:
        payment = self.__repository.find_one(payment_id, user.id)

        if not payment:
            raise PaymentNotFound(f"Cannot find a payment with id {payment_id}")

        return payment

    async def confirm(self, payment_id: int, user: User) -> Payment:
        payment = self.__find_payment_by(payment_id=payment_id, user=user)

        await sleep(3)

        payment.confirm()

        self.__repository.save(payment=payment)

        return payment

    async def cancel(self, payment_id: int, user: User) -> Payment:
        payment = self.__find_payment_by(payment_id=payment_id, user=user)

        await sleep(3)

        payment.cancel()

        self.__repository.save(payment=payment)

        return payment
