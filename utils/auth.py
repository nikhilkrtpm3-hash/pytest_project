import requests
from utils.config import BASE_URL, USERNAME, PASSWORD


def get_token():
    url = f"{BASE_URL}/login"

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        raise Exception("Auth failed")

    return response.json().get("token")