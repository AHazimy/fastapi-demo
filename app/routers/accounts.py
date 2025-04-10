from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.account import AccountModel
from ..schemas.account import AccountCreate, AccountUpdate, Account
from ..database import get_db

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("", response_model=Account)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    db_account = AccountModel(name=account.name, balance=account.balance, email=account.email, phone=account.phone)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.get("/{account_id}", response_model=Account)
def get_account(account_id: int, db: Session = Depends(get_db)):
    account = db.query(AccountModel).filter(AccountModel.id == account_id).first()
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.put("/{account_id}", response_model=Account)
def update_account(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = db.query(AccountModel).filter(AccountModel.id == account_id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    
    update_account_data = account.dict(exclude_unset=True)
    for key, value in update_account_data.items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account