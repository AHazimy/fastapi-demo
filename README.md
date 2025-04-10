# FastAPI Project

This FastAPI application implements Create, Update, and Get operations for Transactions and Accounts. It uses SQLAlchemy for database interactions and Pydantic for data validation.

In addition to the current functionality, the project now includes several improvements and extra features:

- **Database Fallback Mechanism:**  
  The application checks for an environment variable called `DATABASE_URL` to obtain the PostgreSQL connection string. If this variable is missing, it will automatically fallback to using SQLite, ensuring seamless local development. Inside Docker Compose, the service is configured to always run with PostgreSQL as defined in the orchestration file.

- **Interactive API Documentation:**
  You can test and interact with the API endpoints using the automatically generated documentation available at [http://localhost:8000/docs]. This interactive UI makes it easier to understand and try out the various endpoints during development.

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
   docker compose build --no-cache
   docker compose up 
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

You can test and explore the API endpoints using the built-in documentation UI available at [http://localhost:8000/docs]. This interactive documentation provides comprehensive details and enables you to execute API calls directly from your browser

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


## Additional Considerations

- **Security:**  
  For enhanced security in production:
  - Consider integrating a secret management solution such as **Azure Key Vault** to store and manage environment variables securely.
  - Follow best practices for securing API endpoints and handling sensitive data.

- **Validation Enhancements:**  
  Future enhancements might include more granular error handling and additional input validators for other fields as needed (such as Email validation, meaningful error message for Unique Phone Number Check, ...).
  