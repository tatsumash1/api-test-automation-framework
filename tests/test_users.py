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

def test_get_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    data = response.json().get("data")
    assert data.get("id") == 2
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
