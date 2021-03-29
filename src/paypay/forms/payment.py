from pydantic import BaseModel, AnyHttpUrl


class CreationPaymentForm(BaseModel):
    user_id: int
    amount: float
    callback: AnyHttpUrl
    subject: str
    ref: str
