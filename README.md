# FastAPI Project

This project is a FastAPI application that implements Create, Update, and Get operations for Transactions and Accounts. It utilizes SQLAlchemy for database interactions and Pydantic for data validation.

## Project Structure

```
fastapi-project
├── app
│   ├── main.py               # Entry point of the FastAPI application
│   ├── enums
│   │   ├── transaction_enums.py        # ENUMs for transactions
│   ├── models
│   │   ├── account.py        # SQLAlchemy model for accounts
│   │   └── transaction.py     # SQLAlchemy model for transactions
│   ├── routers
│   │   ├── accounts.py       # API routes for account operations
│   │   └── transactions.py    # API routes for transaction operations
│   ├── schemas
│   │   ├── account.py        # Pydantic schema for account validation
│   │   └── transaction.py     # Pydantic schema for transaction validation
│   └── database.py           # Database connection setup
│── tests
│   ├── conftest.py        # SQLAlchemy model for accounts
│   └── test_api.py     # SQLAlchemy model for transactions
├── Dockerfile          
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

## API Usage

### Accounts

- **Create Account**
  - **Endpoint:** `POST /accounts`
  - **Request Body:** Account data (name, balance)
  
- **Update Account**
  - **Endpoint:** `PUT /accounts/{id}`
  - **Request Body:** Updated account data

- **Get Account**
  - **Endpoint:** `GET /accounts/{id}`
  - **Response:** Account details

### Transactions

- **Create Transaction**
  - **Endpoint:** `POST /transactions`
  - **Request Body:** Transaction data (account_id, amount)

- **Get All Transactions**
  - **Endpoint:** `GET /transactions`
  - **Response:** Transaction details
  
- **Get Account's Transactions**
  - **Endpoint:** `GET /transactions/{account_id}`
  - **Response:** Transaction details