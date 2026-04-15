import requests
from utils.config import BASE_URL


def get_token():
    url = f"{BASE_URL}/login"

    payload = {"name":"test", "password":"123"}

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception("Auth failed")

    return response.json().get("token")