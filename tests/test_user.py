import requests

from api.endpoints import create_account
from utils.helpers import load_test_data
from utils.config import  HEADERS,BASE_URL

def test_create_user(api_client):
    data = load_test_data()

    payload = data["user"]
    print()
    url=f"{BASE_URL}{create_account}"
    print(url)
    response = requests.post(url, data=payload, headers=HEADERS)
    data1=response.json()
    print(data1)
    assert response.status_code == 200
    assert data1["responseCode"] == 400
    assert data1["message"] == "Email already exists!"
