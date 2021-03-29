from src.paypay.forms.payment import CreationPaymentForm
from src.paypay.models.payment import Payment, PaymentExtraInfo
from src.paypay.models.user import User


class CreationPaymentToPayment:
    def convert(self, form: CreationPaymentForm, user: User) -> Payment:
        return Payment(
            owner=user,
            ref=form.ref,
            amount=form.amount,
            info=PaymentExtraInfo(
                callback=form.callback
            ),
        )
