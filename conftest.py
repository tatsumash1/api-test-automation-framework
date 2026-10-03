import os

import pytest

from clients.reqres_client import ReqresClient


@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"


@pytest.fixture(scope="session")
def reqres_client(base_url):
    return ReqresClient(
        base_url=base_url,
        api_key=os.getenv("REQRES_API_KEY"),
    )
