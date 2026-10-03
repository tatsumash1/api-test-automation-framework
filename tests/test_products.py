import os

import pytest


def require_api_key():
    if not os.getenv("REQRES_API_KEY"):
        pytest.skip("REQRES_API_KEY is required for this endpoint")


def test_get_list_resources(reqres_client):
    response = reqres_client.get_resources()
    assert response.status_code == 200
    data = response.json()["data"]
    assert data

    for resource in data:
        assert "id" in resource
        assert "name" in resource
        assert "year" in resource
        assert "color" in resource
        assert "pantone_value" in resource


@pytest.mark.parametrize("page_id", [1, 2, 3, 4, 5])
def test_get_product_list(page_id, reqres_client):
    require_api_key()
    response = reqres_client.get_products(page_id)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data

    for product in data:
        assert "id" in product
        assert "name" in product
        assert "year" in product
        assert "color" in product
        assert "pantone_value" in product


@pytest.mark.parametrize("product_id", [1, 2, 3, 4, 5])
def test_get_product(product_id, reqres_client):
    require_api_key()
    response = reqres_client.get_product(product_id)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["id"] == product_id
    assert "name" in data
    assert "year" in data
    assert "color" in data
    assert "pantone_value" in data
