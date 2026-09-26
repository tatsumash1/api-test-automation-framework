import os

import pytest
import requests


BASE_URL = "https://reqres.in/api"
REQUEST_TIMEOUT = 10


def api_headers():
    api_key = os.getenv("REQRES_API_KEY")
    return {"x-api-key": api_key} if api_key else {}


def request(method, path, **kwargs):
    return requests.request(
        method,
        f"{BASE_URL}{path}",
        headers=api_headers(),
        timeout=REQUEST_TIMEOUT,
        **kwargs,
    )


def require_api_key():
    if not os.getenv("REQRES_API_KEY"):
        pytest.skip("REQRES_API_KEY is required for this endpoint")

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user(user_id):
    response = request("GET", f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json().get("data")
    assert data["id"] == user_id
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data

def test_response_from_server():
    response = request("GET", "/users/2")
    assert response.status_code == 200

def test_get_single_user():
    response = request("GET", "/users/2")
    assert response.status_code == 200
    data = response.json().get("data")
    assert data.get("id") == 2
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data

def test_get_user_2():
    response = request("GET", "/users?page=2")
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    assert "id" in data[0]
    assert "email" in data[1]
    assert "first_name" in data[2]
    assert "last_name" in data[3]
    assert "avatar" in data[4]

def test_get_list_resources():
    response = request("GET", "/unknown")
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[1]
    assert "year" in data[2]
    assert "color" in data[3]
    assert "pantone_value" in data[4]

def test_get_products():
    require_api_key()
    response = request("GET", "/products?page=1")
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[1]
    assert "year" in data[2]
    assert "color" in data[3]
    assert "pantone_value" in data[4]

def test_get_single_product():
    require_api_key()
    response = request("GET", "/products/2")
    assert response.status_code == 200
    data = response.json().get("data")
    assert data.get("id") == 2
    assert "name" in data
    assert "year" in data
    assert "color" in data
    assert "pantone_value" in data

## POST requests
def test_post_register_success():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = request("POST", "/register", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "token" in data

def test_post_login_success():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = request("POST", "/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

def test_put_update_user():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = request("PUT", "/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

def test_delete_user():
    response = request("DELETE", "/users/2")
    assert response.status_code == 204

def test_patch_update_user_name():
    payload = {
        "name": "morpheus"
    }
    response = request("PATCH", "/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert "updatedAt" in data

def test_patch_update_user_job():
    payload = {
        "job": "zion resident"
    }
    response = request("PATCH", "/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

def test_patch_update_user_name_and_job():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = request("PATCH", "/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

#Негативные тесты

def test_post_register_unsuccessful():
    payload = {
        "email": "sydney@fife"
    }
    response = request("POST", "/register", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

def test_post_login_unsuccessful():
    payload = {
        "email": "peter@klaven"
    }
    response = request("POST", "/login", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data