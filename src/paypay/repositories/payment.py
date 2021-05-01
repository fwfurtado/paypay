from typing import Optional

from sqlalchemy.orm import Session
from src.paypay.models.payment import Payment
from src.paypay.models.user import User


class PaymentRepository:
    def __init__(self, session: Session):
        self.__session = session

    def save(self, payment: Payment):
        if not payment.id:
            self.__session.add(payment)
        else:
            self.__session.merge(payment)

    def anyone_is_same(self, payment: Payment) -> bool:
        for existing_payment in (
            self.__session.query(Payment)
            .join(User, User.id == Payment.owner_id)
            .filter(Payment.owner_id == payment.owner_id)
            .all()
        ):
            if existing_payment.is_same(payment):
                return True

        return False

    def find_one(self, payment_id: int, owner_id: int) -> Optional[Payment]:
        return (
            self.__session.query(Payment)
            .join(User, User.id == Payment.owner_id)
            .filter(Payment.id == payment_id, Payment.owner_id == owner_id)
            .one_or_none()
        )
