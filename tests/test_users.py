import os

import pytest

def require_api_key():
    if not os.getenv("REQRES_API_KEY"):
        pytest.skip("REQRES_API_KEY is required for this endpoint")

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user(user_id, api_request):
    response = api_request("GET", f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json().get("data")
    assert data["id"] == user_id
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data

@pytest.mark.parametrize("page_id", [1, 2])
def test_get_user_list(page_id, api_request):
    response = api_request("GET", f"/users?page={page_id}")
    assert response.status_code == 200
    data = response.json().get("data")
    assert data
    
    for user in data:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user

def test_get_list_resources(api_request):
    response = api_request("GET", f"/unknown")
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    for resources in data:
    
        assert "id" in resources
        assert "name" in resources
        assert "year" in resources
        assert "color" in resources
        assert "pantone_value" in resources

@pytest.mark.parametrize("p_page_id", [1, 2, 3, 4, 5])
def test_get_product_list(p_page_id, api_request):
    require_api_key()
    response = api_request("GET", f"/products?page={p_page_id}")
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    for product in data:
    
        assert "id" in product
        assert "name" in product
        assert "year" in product
        assert "color" in product
        assert "pantone_value" in product

@pytest.mark.parametrize("product_id", [1, 2, 3, 4, 5])
def test_get_product(product_id, api_request):
    require_api_key()
    response = api_request("GET", f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json().get("data")
    assert data.get("id") == product_id
    assert "name" in data
    assert "year" in data
    assert "color" in data
    assert "pantone_value" in data

## POST requests
def test_post_register_success(api_request):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = api_request("POST", "/register", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "token" in data

def test_post_login_success(api_request):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = api_request("POST", "/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

# PUT request
def test_put_update_user(api_request):
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = api_request("PUT", "/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

# DELETE request
def test_delete_user(api_request):
    response = api_request("DELETE", "/users/2")
    assert response.status_code == 204

# PATCH requests
def test_patch_update_user_name(api_request):
    payload = {
        "name": "morpheus"
    }
    response = api_request("PATCH", "/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert "updatedAt" in data

def test_patch_update_user_job(api_request):
    payload = {
        "job": "zion resident"
    }
    response = api_request("PATCH", "/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

def test_patch_update_user_name_and_job(api_request):
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = api_request("PATCH", "/users/2", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

#Негативные тесты
def test_get_invalid_user(api_request):
    response = api_request("GET", "/users/2500")
    assert response.status_code == 404


def test_post_register_unsuccessful(api_request):
    payload = {
        "email": "sydney@fife"
    }
    response = api_request("POST", "/register", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

def test_post_login_unsuccessful(api_request):
    payload = {
        "email": "peter@klaven"
    }
    response = api_request("POST", "/login", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data