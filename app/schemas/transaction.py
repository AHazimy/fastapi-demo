from pydantic import BaseModel
from datetime import datetime
from app.enums.transaction_enums import TransactionType


class TransactionCreate(BaseModel):
    account_id: int
    amount: float
    transaction_type: TransactionType

class Transaction(BaseModel):
    id: int
    account_id: int
    amount: float
    transaction_type: str
    timestamp: datetime

    class Config:
        orm_mode = True