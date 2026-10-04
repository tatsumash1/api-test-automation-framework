import os

import pytest
import requests

from clients.reqres_client import ReqresClient


@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"


@pytest.fixture(scope="session")
def reqres_client(base_url, api_session):
    return ReqresClient(
        base_url=base_url,
        session=api_session,
        api_key=os.getenv("REQRES_API_KEY"),
    )

@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()

    yield session

    session.close()
