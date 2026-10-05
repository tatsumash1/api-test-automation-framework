import os
from jsonschema import validate
from schemas.products_schemas import PRODUCT_SCHEMA, PRODUCT_LIST_SCHEMA

import pytest


def require_api_key():
    if not os.getenv("REQRES_API_KEY"):
        pytest.skip("REQRES_API_KEY is required for this endpoint")


def test_get_list_resources(reqres_client):
    response = reqres_client.get_resources()

    assert response.status_code == 200

    data = response.json()["data"]
    validate(instance=data, schema=PRODUCT_LIST_SCHEMA)

@pytest.mark.parametrize("page_id", [1, 2, 3, 4, 5])
def test_get_product_list(page_id, reqres_client):
    require_api_key()
    response = reqres_client.get_products(page_id)

    assert response.status_code == 200

    data = response.json()["data"]

    validate(instance=data, schema=PRODUCT_LIST_SCHEMA)


@pytest.mark.parametrize("product_id", [1, 2, 3, 4, 5])
def test_get_product(product_id, reqres_client):
    require_api_key()
    response = reqres_client.get_product(product_id)

    assert response.status_code == 200

    data = response.json()["data"]
    assert data["id"] == product_id

    validate(instance=data, schema=PRODUCT_SCHEMA)
