from typing import Optional
from pydantic import AnyHttpUrl, BaseModel


class CreationPaymentForm(BaseModel):
    amount: float
    ref: str
    callback: Optional[AnyHttpUrl] = None
