import requests

from utils.logger import logger
from api.endpoints import create_account
from api.endpoints import get_user_by_email
from utils.helpers import load_test_data
from utils.config import  HEADERS

def test_create_user(api_client):
    data = load_test_data()
    payload = data["user"]
    logger.debug("Creating user with endpoint: %s", create_account)
    response = api_client.post(create_account,payload, HEADERS)
    data1=response.json()
    logger.debug("Create-user response status: %s", response.status_code)
    logger.debug("Create-user response code: %s", data1.get("responseCode"))
    print(data1)
    assert response.status_code == 200
    if response.status_code == 200:
        logger.info("user created successfully")
    else:
        logger.info("user not created successfully")
    assert data1["responseCode"] == 400
    assert data1["message"] == "Email already exists!"

def test_get_userbyemail(api_client):
    data = load_test_data()
    param1={
        "email": data["email"]
    }
    logger.debug("Looking up user by email with endpoint: %s", get_user_by_email)

    response = api_client.get(
        get_user_by_email,
        HEADERS,
        params = param1
    )
    user_json = response.json()
    logger.debug("Get-user response status: %s", response.status_code)
    logger.debug("Get-user response code: %s", user_json.get("responseCode"))
    print(user_json)

    assert response.status_code == 200
    if response.status_code == 200:
        logger.info("user found with the give email")
    else:
        logger.info("user not found with the give email")
    assert user_json["responseCode"] == 200
    assert user_json["user"]["email"] == data["email"]
