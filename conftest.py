import pytest
from api.api_clients import APIClient

BASE_URL = "https://automationexercise.com/api"

@pytest.fixture
def api_client():
    return APIClient(BASE_URL)