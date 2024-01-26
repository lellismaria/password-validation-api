import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_validacao_tamanho():
    response = client.post("/validate_password", json={"password": "abc123"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": {
            "status": 400,
            "message": "A senha deve conter ao menos nove caracteres.",
            "isValid": False
        }
    }

def test_validacao_sem_minuscula():
    response = client.post("/validate_password", json={"password": "AAABBBCCC"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": {
            "status": 400,
            "message": "A senha deve conter ao menos uma letra minúscula.",
            "isValid": False
        }
    }

def test_validacao_sem_maiuscula():
    response = client.post("/validate_password", json={"password": "aaabbbccc"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": {
            "status": 400,
            "message": "A senha deve conter ao menos uma letra maiúscula.",
            "isValid": False
        }
    }

def test_validacao_sem_numero():
    response = client.post("/validate_password", json={"password": "AbTpo!foo"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": {
            "status": 400,
            "message": "A senha deve conter ao menos um número.",
            "isValid": False
        }
    }

def test_validacao_sem_caracter_especial():
    response = client.post("/validate_password", json={"password": "AbTp9 fok"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": {
            "status": 400,
            "message": "A senha deve conter ao menos um caractere especial.",
            "isValid": False
        }
    }

def test_validacao_sem_caracter_repetido():
    response = client.post("/validate_password", json={"password": "AbTp9!foA"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": {
            "status": 400,
            "message": "A senha não deve conter caracteres repetidos.",
            "isValid": False
        }
    }

def test_validacao():
    response = client.post("/validate_password", json={"password": "AbTp9!fok"})
    assert response.status_code == 200
    assert response.json() == {
        "status": 200,
        "message": "A senha é válida.",
        "isValid": True
    }