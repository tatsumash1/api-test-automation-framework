import pytest

from jsonschema import validate
from schemas.auth_schemas import REGISTER_SUCCESS_SCHEMA, LOGIN_SUCCESS_SCHEMA, AUTH_ERROR_SCHEMA

def test_post_register_success(reqres_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    }
    response = reqres_client.register(payload)

    assert response.status_code == 200
    
    data = response.json()
    validate(instance=data, schema=REGISTER_SUCCESS_SCHEMA)


def test_post_login_success(reqres_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }
    response = reqres_client.login(payload)

    assert response.status_code == 200

    data = response.json()
    validate(instance=data, schema=LOGIN_SUCCESS_SCHEMA)


# def test_post_register_unsuccessful(reqres_client):
#     payload = {"email": "sydney@fife"}
#     response = reqres_client.register(payload)

#     assert response.status_code == 400

#     data = response.json()
#     validate(instance=data, schema=AUTH_ERROR_SCHEMA)


# def test_post_login_unsuccessful(reqres_client):
#     payload = {"email": "peter@klaven"}
#     response = reqres_client.login(payload)
#     assert response.status_code == 400
#     data = response.json()
#     assert "error" in data

@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"email": "sydney@fife"},
        {"password": "pistol"},
        {"email": "", "password": ""},
    ],
    ids=[
        "empty_payload",
        "missing_password",
        "missing_email",
        "empty_email_and_password",
    ],
)
def test_register_with_invalid_data(reqres_client, payload):
    response = reqres_client.register(payload)

    assert response.status_code == 400

    data = response.json()
    validate(instance=data, schema=AUTH_ERROR_SCHEMA)