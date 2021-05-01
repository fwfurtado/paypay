from fastapi import Depends, APIRouter, Path

from src.paypay.entrypoint.http.dependencies.commons import oauth_scheme
from src.paypay.entrypoint.http.dependencies.payment import payment_controller
from src.paypay.entrypoint.http.dependencies.user import load_user
from src.paypay.controllers.payment import PaymentController
from src.paypay.models.payment import Payment
from src.paypay.models.user import User
from src.paypay.forms.payment import CreationPaymentForm

router = APIRouter(prefix="/payments", dependencies=[Depends(oauth_scheme)])


@router.post(path="/", status_code=201)
async def create(
    form: CreationPaymentForm,
    controller: PaymentController = Depends(payment_controller),
    current_user: User = Depends(load_user),
) -> Payment:
    return await controller.bank_slip_pay(form=form, user=current_user)


@router.post(path="/online", status_code=201)
async def tries_to_pay(
    form: CreationPaymentForm,
    controller: PaymentController = Depends(payment_controller),
    current_user: User = Depends(load_user),
) -> Payment:
    return await controller.online_pay(form=form, user=current_user)


@router.put(path="/{payment_id}/confirm", status_code=202)
async def confirm(
    *,
    payment_id: int = Path(
        default=None, title="The id of  the payment you want to confirm", gt=0
    ),
    controller: PaymentController = Depends(payment_controller),
    current_user: User = Depends(load_user),
) -> Payment:
    return await controller.confirm(payment_id=payment_id, user=current_user)


@router.delete(path="/{payment_id}", status_code=204)
async def cancel(
    *,
    payment_id: int = Path(
        default=None, title="The id of  the payment you want to cancel", gt=0
    ),
    controller: PaymentController = Depends(payment_controller),
    current_user: User = Depends(load_user),
) -> Payment:
    return await controller.cancel(payment_id=payment_id, user=current_user)
