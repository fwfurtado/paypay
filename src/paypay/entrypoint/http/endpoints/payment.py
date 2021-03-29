from fastapi import Depends, APIRouter
from src.paypay.controllers.payment import PaymentController
from src.paypay.entrypoint.http.dependencies.payment import payment_controller
from src.paypay.models.payment import Payment
from src.paypay.forms.payment import CreationPaymentForm

router = APIRouter(prefix="/payments")


@router.post(path="/", status_code=201)
async def tries_to_pay(
    form: CreationPaymentForm,
    controller: PaymentController = Depends(payment_controller),
) -> Payment:
    return await controller.pay(form=form)
