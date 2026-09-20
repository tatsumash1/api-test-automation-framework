import requests

#GET /api/users/2
"""
HTTP status == 200

data.id == 2

data.email существует

data.first_name существует

data.last_name существует
"""
def test_response_from_server():
    response = requests.get("https://reqres.in/api")
    print(response)

def test_get_single_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    data = response.json().get("data")
    assert data.get("id") == 2
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data

def test_get_user():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    assert "id" in data[0]
    assert "email" in data[1]
    assert "first_name" in data[2]
    assert "last_name" in data[3]
    assert "avatar" in data[4]

def test_get_list_resources():
    response = requests.get("https://reqres.in/api/unknown")
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[1]
    assert "year" in data[2]
    assert "color" in data[3]
    assert "pantone_value" in data[4]

def test_get_products():
    response = requests.get("https://reqres.in/api/products?page=1")
    assert response.status_code == 200
    data = response.json().get("data")
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[1]
    assert "year" in data[2]
    assert "color" in data[3]
    assert "pantone_value" in data[4]

def test_get_single_product():
    response = requests.get("https://reqres.in/api/products/2")
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
    response = requests.post("https://reqres.in/api/register", json=payload)
    assert response.status_code == 200
    data = response.json().get("data")
    assert "id" in data
    assert "token" in data

def test_post_login_success():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post("https://reqres.in/api/login", json=payload)
    assert response.status_code == 200
    data = response.json().get("data")
    assert "token" in data

def test_put_update_user():
    payload = {
        "email": "morpheus",
        "job": "zion resident"
    }
    response = requests.put("https://reqres.in/api/users/2")
    assert response.status_code == 200
    data = response.json().get("data")
    assert "id" in data
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "avatar" in data

def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204