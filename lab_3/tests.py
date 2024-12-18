import pytest
import httpx


API_PREFIX = f"http://localhost:8000/api"


@pytest.fixture
def client():
    with httpx.Client(base_url=API_PREFIX) as client:
        yield client


def test_hash_code(client):
    params = {"s": "test"}
    response = client.get("/hash_code", params=params)

    assert response.status_code == 200
    data = response.json()

    assert "answer" in data


def test_caesar_cipher(client):
    params = {"s": "hello"}
    response = client.get("/caesar_cipher", params=params)

    assert response.status_code == 200
    data = response.json()

    assert "answer" in data
    assert data["answer"] == "khoor"


def test_caesar_cipher_with_special_characters(client):
    params = {"s": "hello world!"}
    response = client.get("/caesar_cipher", params=params)

    assert response.status_code == 200
    data = response.json()

    assert data["answer"] == "khoor zruog!"
