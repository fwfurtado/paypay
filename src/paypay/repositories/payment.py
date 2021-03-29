from typing import Dict, Optional

from src.paypay.models.payment import Payment


class PaymentRepository:
    IDENTITY: int = 0
    DB: Dict[int, Payment] = dict()

    def save(self, payment: Payment):
        PaymentRepository.IDENTITY += 1
        payment.id = PaymentRepository.IDENTITY
        PaymentRepository.DB[PaymentRepository.IDENTITY] = payment

    def anyone_is_same(self, payment: Payment) -> bool:
        return len([p for p in PaymentRepository.DB.values() if p.is_same(payment)]) > 0

    def find_one(self, payment_id: int) -> Optional[Payment]:
        return PaymentRepository.DB.get(payment_id, None)

    def update(self, payment: Payment) -> bool:
        payment_id = payment.id

        if payment_id not in PaymentRepository.DB:
            return False

        PaymentRepository.DB[payment_id] = payment
        return True
