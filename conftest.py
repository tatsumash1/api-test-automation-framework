import pytest

import os
import requests

REQUESTS_TIMEOUT = 10

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"

@pytest.fixture(scope="session")
def api_request(base_url):
    def send(method, path, **kwargs):
        api_key = os.getenv("REQRES_API_KEY")
        headers = {"x-api-key": api_key} if api_key else {}

        return requests.request(
            method,
            f"{base_url}{path}",
            headers = headers,
            timeout=REQUESTS_TIMEOUT,
            **kwargs,
        )

    return send