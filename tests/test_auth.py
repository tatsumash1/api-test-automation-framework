import pytest

from jsonschema import validate
from schemas.auth_schemas import REGISTER_SUCCESS_SCHEMA, LOGIN_SUCCESS_SCHEMA, AUTH_ERROR_SCHEMA

@pytest.mark.auth
@pytest.mark.smoke
def test_post_register_success(reqres_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    }
    response = reqres_client.register(payload)

    assert response.status_code == 200
    
    data = response.json()
    validate(instance=data, schema=REGISTER_SUCCESS_SCHEMA)

@pytest.mark.auth
@pytest.mark.smoke
def test_post_login_success(reqres_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }
    response = reqres_client.login(payload)

    assert response.status_code == 200

    data = response.json()
    validate(instance=data, schema=LOGIN_SUCCESS_SCHEMA)

@pytest.mark.auth
@pytest.mark.negative
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
    assert "error" in data
    validate(instance=data,
            schema=AUTH_ERROR_SCHEMA,
    )