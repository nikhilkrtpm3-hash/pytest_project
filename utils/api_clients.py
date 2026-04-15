import requests


class APIClient:

    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def get_headers(self):
        headers = {"Content-Type": "application/json"}

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint, headers=self.get_headers())

    def post(self, endpoint, payload=None):
        return requests.post(self.base_url + endpoint, json=payload, headers=self.get_headers())

    def put(self, endpoint, payload=None):
        return requests.put(self.base_url + endpoint, json=payload, headers=self.get_headers())

    def delete(self, endpoint):
        return requests.delete(self.base_url + endpoint, headers=self.get_headers())
