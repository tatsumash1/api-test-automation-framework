import os

import pytest
import requests


REQUEST_TIMEOUT = 10


def api_headers():
    api_key = os.getenv("REQRES_API_KEY")
    return {"x-api-key": api_key} if api_key else {}


def request(method, path, base_url, **kwargs):
    return requests.request(
        method,
        f"{base_url}{path}",
        headers=api_headers(),
        timeout=REQUEST_TIMEOUT,
        **kwargs,
    )


def require_api_key():
    if not os.getenv("REQRES_API_KEY"):
        pytest.skip("REQRES_API_KEY is required for this endpoint")

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user(user_id, base_url):
    response = request("GET", f"/users/{user_id}", base_url=base_url)
    assert response.status_code == 200
    data = response.json().get("data")
    assert data["id"] == user_id
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data

@pytest.mark.parametrize("page_id", [1, 2])
def test_get_user_list(page_id, base_url):
    response = request("GET", f"/users?page={page_id}", base_url=base_url)
    assert response.status_code == 200
    data = response.json().get("data")
    assert data
    
    for user in data:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user

def test_get_list_resources(base_url):
    response = request("GET", f"/unknown", base_url=base_url)
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    for resources in data:
    
        assert "id" in data
        assert "name" in data
        assert "year" in data
        assert "color" in data
        assert "pantone_value" in data

@pytest.mark.parametrize("p_page_id", [1, 2, 3, 4, 5])
def test_get_product_list(p_page_id, base_url):
    require_api_key()
    response = request("GET", f"/products?page={p_page_id}", base_url=base_url)
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    for product in data:
    
        assert "id" in data
        assert "name" in data
        assert "year" in data
        assert "color" in data
        assert "pantone_value" in data

@pytest.mark.parametrize("product_id", [1, 2, 3, 4, 5])
def test_get_product(product_id, base_url):
    require_api_key()
    response = request("GET", f"/products/{product_id}", base_url=base_url)
    assert response.status_code == 200
    data = response.json().get("data")
    assert data.get("id") == product_id
    assert "name" in data
    assert "year" in data
    assert "color" in data
    assert "pantone_value" in data

## POST requests
def test_post_register_success(base_url):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = request("POST", "/register", json=payload, base_url=base_url)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "token" in data

def test_post_login_success(base_url):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = request("POST", "/login", json=payload, base_url=base_url)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

# PUT request
def test_put_update_user(base_url):
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = request("PUT", "/users/2", json=payload, base_url=base_url)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

# DELETE request
def test_delete_user(base_url):
    response = request("DELETE", "/users/2", base_url=base_url)
    assert response.status_code == 204

# PATCH requests
def test_patch_update_user_name(base_url):
    payload = {
        "name": "morpheus"
    }
    response = request("PATCH", "/users/2", json=payload, base_url=base_url)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert "updatedAt" in data

def test_patch_update_user_job(base_url):
    payload = {
        "job": "zion resident"
    }
    response = request("PATCH", "/users/2", json=payload, base_url=base_url)
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

def test_patch_update_user_name_and_job(base_url):
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = request("PATCH", "/users/2", json=payload, base_url=base_url)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

#Негативные тесты
def test_get_invalid_user(base_url):
    response = request("GET", "/users/2500", base_url=base_url)
    assert response.status_code == 404


def test_post_register_unsuccessful(base_url):
    payload = {
        "email": "sydney@fife"
    }
    response = request("POST", "/register", json=payload, base_url=base_url)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

def test_post_login_unsuccessful(base_url):
    payload = {
        "email": "peter@klaven"
    }
    response = request("POST", "/login", json=payload, base_url=base_url)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data