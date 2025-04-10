from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.transaction import TransactionModel
from app.models.account import AccountModel
from app.schemas.transaction import TransactionCreate, Transaction
from app.database import get_db

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    account = db.query(AccountModel).filter(AccountModel.id == transaction.account_id).first()
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    db_transaction = TransactionModel(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/{account_id}", response_model=List[Transaction])
def get_transaction(account_id: int, db: Session = Depends(get_db)):
    db_transaction = db.query(TransactionModel).filter(TransactionModel.account_id == account_id).all()
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@router.get("", response_model=list[Transaction])
def get_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = db.query(TransactionModel).offset(skip).limit(limit).all()
    return transactions