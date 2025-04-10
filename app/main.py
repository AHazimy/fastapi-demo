from fastapi import FastAPI
from app.routers import accounts, transactions
from app.database import engine, Base
from app.models import AccountModel, TransactionModel
from app.models.transaction import TransactionModel
from app.models.account import AccountModel

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(accounts.router)
app.include_router(transactions.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the test FastAPI project!"}