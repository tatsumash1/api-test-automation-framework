def test_post_register_success(reqres_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    }
    response = reqres_client.register(payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "token" in data


def test_post_login_success(reqres_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }
    response = reqres_client.login(payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data


def test_post_register_unsuccessful(reqres_client):
    payload = {"email": "sydney@fife"}
    response = reqres_client.register(payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data


def test_post_login_unsuccessful(reqres_client):
    payload = {"email": "peter@klaven"}
    response = reqres_client.login(payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

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
    assert isinstance(data["error"], str)