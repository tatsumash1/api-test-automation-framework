from unittest.mock import Mock

import pytest
import os
import requests

from clients.reqres_client import ReqresClient

from clients.reqres_client import ApiRequestError


pytestmark = pytest.mark.unit

@pytest.fixture(scope="session")
def reqres_client(base_url, api_session, request_timeout):
    return ReqresClient(
        base_url=base_url,
        session=api_session,
        api_key=os.getenv("REQRES_API_KEY"),
        timeout=request_timeout,
    )

@pytest.fixture
def client_and_session():
    session = Mock()
    client = ReqresClient(
        base_url="https://example.test/api",
        session=session,
        api_key="test-key",
        timeout=5,
    )
    return client, session


def test_get_user_builds_request(client_and_session):
    client, session = client_and_session

    client.get_user(2)

    session.request.assert_called_once_with(
        "GET",
        "https://example.test/api/users/2",
        headers={"x-api-key": "test-key"},
        timeout=5,
    )


def test_register_sends_json_payload(client_and_session):
    client, session = client_and_session
    payload = {"email": "test@example.com", "password": "secret"}

    client.register(payload)

    session.request.assert_called_once_with(
        "POST",
        "https://example.test/api/register",
        headers={"x-api-key": "test-key"},
        timeout=5,
        json=payload,
    )


@pytest.mark.parametrize(
    "method_name, expected_method, expected_path",
    [
        ("get_users", "GET", "/users?page=2"),
        ("get_resources", "GET", "/unknown"),
        ("get_products", "GET", "/products?page=2"),
        ("get_product", "GET", "/products/7"),
        ("login", "POST", "/login"),
        ("update_user", "PUT", "/users/2"),
        ("patch_user", "PATCH", "/users/2"),
        ("delete_user", "DELETE", "/users/2"),
        ("create_user", "POST", "/users"),
    ],
)
def test_client_endpoint_methods(method_name, expected_method, expected_path, client_and_session):
    client, session = client_and_session
    method = getattr(client, method_name)

    if method_name in {"get_users", "get_products"}:
        method(2)
    elif method_name in {"get_product", "get_user", "delete_user"}:
        method(2 if method_name != "get_product" else 7)
    elif method_name == "get_resources":
        method()
    elif method_name == "login":
        method({"email": "test@example.com"})
    else:
        method(2, {"name": "morpheus"}) if method_name != "create_user" else method({"name": "morpheus"})

    call = session.request.call_args
    assert call.args[:2] == (expected_method, f"https://example.test/api{expected_path}")
    assert call.kwargs["headers"] == {"x-api-key": "test-key"}
    assert call.kwargs["timeout"] == 5

def test_client_handles_timeout(client_and_session):
    client, session = client_and_session

    session.request.side_effect = requests.exceptions.ReadTimeout(
        "server did not respond"
    )

    with pytest.raises(ApiRequestError, match="Таймаут"):
        client.get_user(2)