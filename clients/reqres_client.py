import requests


class ReqresClient:
    def __init__(self, base_url, api_key=None, timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.headers = {"x-api-key": api_key} if api_key else {}

    def _request(self, method, path, **kwargs):
        return requests.request(
            method,
            f"{self.base_url}{path}",
            headers=self.headers,
            timeout=self.timeout,
            **kwargs,
        )

    def get_user(self, user_id):
        return self._request("GET", f"/users/{user_id}")

    def get_users(self, page):
        return self._request("GET", f"/users?page={page}")

    def get_resources(self):
        return self._request("GET", "/unknown")

    def get_products(self, page):
        return self._request("GET", f"/products?page={page}")

    def get_product(self, product_id):
        return self._request("GET", f"/products/{product_id}")

    def register(self, payload):
        return self._request("POST", "/register", json=payload)

    def login(self, payload):
        return self._request("POST", "/login", json=payload)

    def update_user(self, user_id, payload):
        return self._request("PUT", f"/users/{user_id}", json=payload)

    def patch_user(self, user_id, payload):
        return self._request("PATCH", f"/users/{user_id}", json=payload)

    def delete_user(self, user_id):
        return self._request("DELETE", f"/users/{user_id}")
