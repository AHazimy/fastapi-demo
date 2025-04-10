# FastAPI Project

This project is a FastAPI application that implements Create, Update, and Get operations for Transactions and Accounts. It utilizes SQLAlchemy for database interactions and Pydantic for data validation.

## Project Structure

```
fastapi-demo
├── app
│   ├── main.py                     # Entry point of the FastAPI application
│   ├── enums
│   │   ├── transaction_enums.py    # ENUMs for transactions
│   ├── models
│   │   ├── account.py              # SQLAlchemy model for accounts
│   │   └── transaction.py          # SQLAlchemy model for transactions
│   ├── routers     
│   │   ├── accounts.py             # API routes for account operations
│   │   └── transactions.py         # API routes for transaction operations
│   ├── schemas     
│   │   ├── account.py              # Pydantic schema for account validation
│   │   └── transaction.py          # Pydantic schema for transaction validation
│   └── database.py                 # Database connection setup
│── tests     
│   ├── conftest.py                 # SQLAlchemy model for accounts
│   └── test_api.py                 # SQLAlchemy model for transactions
├── Dockerfile                      # Container Build
├── docker-compose.yml              # Service Orchestration
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

# Setup Instructions

You can run the application in two ways: **Manually** or using **Docker Compose**. Choose the option that best fits your environment.

---

## Option 1: Running Manually

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AHazimy/fastapi-demo.git
   cd fastapi-demo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests:**
   ```bash
   pytest --maxfail=1 --disable-warnings -q
   ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Option 2: Running with Docker Compose

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AHazimy/fastapi-demo.git
   cd fastapi-demo
   ```

2. **Build and start the services:**
   ```bash
   docker-compose up --build
   ```

   This command will start both the web application and the PostgreSQL database services defined in the Docker Compose file.

3. **To stop the services, run:**
   ```bash
   docker-compose down
   ```
  
4. **To run the test:**
   ```bash
   docker build --no-cache -t fastapi-test-project .
   docker run --rm fastapi-test-project pytest --disable-warnings -q
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



