from datetime import datetime, timedelta
from enum import Enum
from typing import Optional
from sqlalchemy import (
    Column,
    String,
    BigInteger,
    Numeric,
    DateTime,
    ForeignKey,
    Enum as OrmENum,
)
from sqlalchemy.orm import relationship

from src.paypay.exeptions.payment import InvalidPaymentStatusTransition
from paypay.infra.database import Base # type: ignore

FIVE_MINUTES = timedelta(minutes=5)


class PaymentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


class PaymentExtraInfo(Base):
    __tablename__ = "payment_extra_infos"
    id: int = Column(BigInteger, primary_key=True) # type: ignore
    attribute: str = Column(String) # type: ignore
    value: str = Column(String) # type: ignore
    payment_id: int = Column(BigInteger, ForeignKey("payments.id")) # type: ignore


class Payment(Base):
    __tablename__ = "payments"

    id: Optional[int] = Column(BigInteger, primary_key=True) # type: ignore
    amount: float = Column(Numeric, nullable=False) # type: ignore
    ref: str = Column(String, nullable=False, index=True) # type: ignore
    status: PaymentStatus = Column(
        OrmENum(PaymentStatus), default=PaymentStatus.SCHEDULED, nullable=False
    ) # type: ignore
    created_at: datetime = Column(DateTime, default=datetime.now, nullable=False) # type: ignore
    info: PaymentExtraInfo = relationship("PaymentExtraInfo", cascade="save-update") # type: ignore
    owner_id: int = Column(BigInteger, ForeignKey("users.id"), nullable=False) # type: ignore

    def confirm(self):
        if self.status != PaymentStatus.SCHEDULED:
            raise InvalidPaymentStatusTransition("Payment not in scheduler")

        if self.amount > 15000:
            self.status = PaymentStatus.CANCELLED
        else:
            self.status = PaymentStatus.CONFIRMED

    def cancel(self):
        if self.status != PaymentStatus.SCHEDULED:
            raise InvalidPaymentStatusTransition("Payment not in scheduler")
        self.status = PaymentStatus.CANCELLED

    def is_same(self, other: "Payment") -> bool:
        time_diff = other.created_at - self.created_at
        return (
            time_diff < FIVE_MINUTES
            and other.amount == self.amount
            and other.ref == self.ref
        )
