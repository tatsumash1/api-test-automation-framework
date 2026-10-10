import pytest
from jsonschema import validate
from schemas.user_schemas import USER_SCHEMA, USER_LIST_SCHEMA, USER_PUT_SCHEMA, USER_PATCH_NAME_SCHEMA, USER_PATCH_JOB_SCHEMA, USER_PATCH_NAME_AND_JOB_SCHEMA


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user(user_id, reqres_client):
    response = reqres_client.get_user(user_id)

    assert response.status_code == 200

    data = response.json()["data"]
    validate(instance=data, schema=USER_SCHEMA)

    assert data["id"] == user_id


@pytest.mark.parametrize("page_id", [1, 2])
def test_get_user_list(page_id, reqres_client):
    response = reqres_client.get_users(page_id)

    assert response.status_code == 200

    data = response.json()["data"]
    validate(instance=data, schema=USER_LIST_SCHEMA)

def test_put_update_user(reqres_client):
    payload = {
        "name": "morpheus",
        "job": "zion resident",
    }

    response = reqres_client.update_user(2, payload)

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=USER_PUT_SCHEMA)

    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]

def test_delete_user(reqres_client):
    response = reqres_client.delete_user(2)

    assert response.status_code == 204

def test_patch_update_user_name(reqres_client):
    payload = {"name": "morpheus"}
    response = reqres_client.patch_user(2, payload)

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=USER_PATCH_NAME_SCHEMA)

    assert data["name"] == payload["name"]
    assert "updatedAt" in data

def test_patch_update_user_job(reqres_client):
    payload = {"job": "zion resident"}
    response = reqres_client.patch_user(2, payload)

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=USER_PATCH_JOB_SCHEMA)

    assert data["job"] == payload["job"]
    assert "updatedAt" in data

def test_patch_update_user_name_and_job(reqres_client):
    payload = {
        "name": "morpheus",
        "job": "zion resident",
    }
    response = reqres_client.patch_user(2, payload)

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=USER_PATCH_NAME_AND_JOB_SCHEMA)
    
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data

def test_get_invalid_user(reqres_client):
    response = reqres_client.get_user(2500)
    assert response.status_code == 404
