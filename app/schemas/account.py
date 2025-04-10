from typing import Optional
from pydantic import BaseModel

class AccountBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    balance: Optional[float] = None
    phone: Optional[str] = None

class AccountCreate(AccountBase):
    name: str
    email: str
    balance: float
    phone: str


class AccountUpdate(AccountBase):
    pass

class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True