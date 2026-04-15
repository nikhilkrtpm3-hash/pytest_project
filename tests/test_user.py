def test_get_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200


def test_create_user(api_client):
    payload = {
        "name": "nikhil",
        "job": "QA Engineer"
    }

    response = api_client.post("/users", payload)

    assert response.status_code == 201