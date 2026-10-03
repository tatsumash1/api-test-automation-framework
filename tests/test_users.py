import pytest


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user(user_id, reqres_client):
    response = reqres_client.get_user(user_id)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["id"] == user_id
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data


@pytest.mark.parametrize("page_id", [1, 2])
def test_get_user_list(page_id, reqres_client):
    response = reqres_client.get_users(page_id)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data

    for user in data:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user


def test_put_update_user(reqres_client):
    payload = {
        "name": "morpheus",
        "job": "zion resident",
    }
    response = reqres_client.update_user(2, payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data


def test_delete_user(reqres_client):
    response = reqres_client.delete_user(2)
    assert response.status_code == 204


def test_patch_update_user_name(reqres_client):
    payload = {"name": "morpheus"}
    response = reqres_client.patch_user(2, payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert "updatedAt" in data


def test_patch_update_user_job(reqres_client):
    payload = {"job": "zion resident"}
    response = reqres_client.patch_user(2, payload)
    assert response.status_code == 200
    data = response.json()
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
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data


def test_get_invalid_user(reqres_client):
    response = reqres_client.get_user(2500)
    assert response.status_code == 404
