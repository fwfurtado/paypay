from typing import Dict

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
