from dataclasses import field, dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, Optional

from src.paypay.models.user import User

FIVE_MINUTES = timedelta(minutes=5)


class PaymentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


@dataclass()
class PaymentExtraInfo:
    callback: str
    info: Dict[str, Any] = field(default_factory=dict)


@dataclass()
class Payment:
    owner: User
    amount: float
    ref: str
    info: PaymentExtraInfo
    status: PaymentStatus = PaymentStatus.SCHEDULED
    id: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.now)

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

    def is_same(self, other: "Payment") -> bool:
        time_diff = other.created_at - self.created_at
        return (
            time_diff < FIVE_MINUTES
            and other.amount == self.amount
            and other.ref == self.ref
        )
