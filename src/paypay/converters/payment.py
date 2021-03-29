from src.paypay.models.payment import Payment, PaymentExtraInfo
from src.paypay.forms.payment import CreationPaymentForm


class CreationPaymentToPayment:
    def convert(self, form: CreationPaymentForm) -> Payment:
        return Payment(
            owner=form.user_id,
            ref=form.ref,
            amount=form.amount,
            info=PaymentExtraInfo(
                callback=form.callback, info={"subject": form.subject}
            ),
        )
