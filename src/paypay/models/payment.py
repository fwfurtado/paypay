from enum import  Enum
from dataclasses import  dataclass

class PaymentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

@dataclass()
class Payment:
    owner: User
    subject: str
    amount: float
    status: PaymentStatus = PaymentStatus.SCHEDULED


    def confirm(self):
        if self.status != PaymentStatus.SCHEDULED:
            raise ValueError("Payment not in scheduler")

        if self.amount > 15000:
            self.status = PaymentStatus.CANCELLED
        else:
            self.status = PaymentStatus.CONFIRMED

    def cancel(self):
        if self.status != PaymentStatus.SCHEDULED:
            raise ValueError("Payment not in scheduler")
        self.status = PaymentStatus.CANCELLED