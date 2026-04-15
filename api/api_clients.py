import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()   # reusable session

    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, headers=headers, params=params)
        return response

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, headers=headers)
        return response

    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        print(url)
        response = self.session.put(url, data=data, headers=headers)
        return response

    def delete(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, data=data, headers=headers)
        return response