import requests


class BaseClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.linear.app/graphql"
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json",
        }

    def _make_request(self, query, variables=None):
        response = requests.post(
            self.base_url,
            headers=self.headers,
            json={"query": query, "variables": variables},
        )

        # Add debugging information
        # print(f"Status Code: {response.status_code}")
        # print(f"Response: {response.text}")

        if response.status_code != 200:
            return None

        return response.json()
