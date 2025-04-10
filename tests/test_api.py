# tests/test_api.py
import pytest

def test_create_account(client):
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "phone": "1234567890",
        "balance": 100.0
    }
    response = client.post("/accounts/", json=payload)
    assert response.status_code in (200, 201)
    data = response.json()
    assert "id" in data
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["phone"] == payload["phone"]
    assert data["balance"] == payload["balance"]

def test_update_account(client):
    create_payload = {
        "name": "Bob",
        "email": "bob@example.com",
        "phone": "0987654321",
        "balance": 50.0
    }
    response = client.post("/accounts/", json=create_payload)
    assert response.status_code in (200, 201)
    account = response.json()
    account_id = account["id"]

    update_payload = {
        "name": "Bob Updated",
        "email": "bob.updated@example.com",
        "phone": "0987654321",
        "balance": 75.0
    }
    response = client.put(f"/accounts/{account_id}", json=update_payload)
    assert response.status_code in (200, 204)
    
    response = client.get(f"/accounts/{account_id}")
    assert response.status_code == 200
    updated_account = response.json()
    assert updated_account["name"] == update_payload["name"]
    assert updated_account["email"] == update_payload["email"]
    assert updated_account["balance"] == update_payload["balance"]

def test_create_transaction(client):
    account_payload = {
        "name": "Charlie",
        "email": "charlie@example.com",
        "phone": "1112223333",
        "balance": 200.0
    }
    response = client.post("/accounts/", json=account_payload)
    assert response.status_code in (200, 201)
    account_id = response.json()["id"]

    transaction_payload = {
        "account_id": account_id,
        "amount": 50.0,
        "transaction_type": "deposit"
    }

    response = client.post("/transactions/", json=transaction_payload)
    assert response.status_code in (200, 201)
    tx_data = response.json()
    assert "id" in tx_data
    assert tx_data["account_id"] == account_id
    assert tx_data["amount"] == transaction_payload["amount"]
    assert tx_data["transaction_type"] == transaction_payload["transaction_type"]

def test_retrieve_transactions(client):
    account_payload = {
        "name": "Daisy",
        "email": "daisy@example.com",
        "phone": "4445556666",
        "balance": 300.0
    }
    response = client.post("/accounts/", json=account_payload)
    assert response.status_code in (200, 201)
    account_id = response.json()["id"]

    tx_payload1 = {
        "account_id": account_id,
        "amount": 30.0,
        "transaction_type": "withdrawal"
    }
    tx_payload2 = {
        "account_id": account_id,
        "amount": 70.0,
        "transaction_type": "deposit"
    }
    client.post("/transactions/", json=tx_payload1)
    client.post("/transactions/", json=tx_payload2)

    response = client.get(f"/transactions/{account_id}", params={"account_id": account_id})
    print(response.json())
    assert response.status_code == 200
    transactions = response.json()
    
    assert isinstance(transactions, list)
    assert len(transactions) >= 2
    print(transactions)
    print(account_id)
    for tx in transactions:
        assert tx["account_id"] == account_id
