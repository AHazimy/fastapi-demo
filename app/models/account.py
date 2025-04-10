from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class AccountModel(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
    balance = Column(Float, default=0.0)
    phone = Column(String, unique=True)

    transactions = relationship("TransactionModel", back_populates="account", cascade="all, delete-orphan")
