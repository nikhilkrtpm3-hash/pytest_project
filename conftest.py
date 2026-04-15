import pytest
from utils.api_clients import APIClient
from utils.auth import get_token
from utils.config import BASE_URL

@pytest.fixture(scope="session")
def auth_token():
    return get_token()

@pytest.fixture(scope="session")
def api_client(auth_token):
    return APIClient(BASE_URL, token=auth_token)