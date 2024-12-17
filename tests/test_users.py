import unittest
from unittest.mock import patch

from linear_python.resources.users import UserClient


class TestUserClient(unittest.TestCase):
    def setUp(self):
        self.client = UserClient("fake-api-key")

    @patch("linear_python.base.requests.post")
    def test_get_user(self, mock_post):
        # Setup mock response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "data": {
                "user": {"id": "user1", "name": "John Doe", "email": "john@example.com"}
            }
        }

        # Make request
        response = self.client.get_user("user1")

        # Assert request was made with correct parameters
        mock_post.assert_called_once()
        self.assertEqual(response["data"]["user"]["id"], "user1")

    @patch("linear_python.base.requests.post")
    def test_get_users(self, mock_post):
        # Setup mock response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "data": {
                "users": {
                    "nodes": [
                        {"id": "user1", "name": "John Doe", "email": "john@example.com"}
                    ]
                }
            }
        }

        # Make request
        response = self.client.get_users()

        # Assert request was made with correct parameters
        mock_post.assert_called_once()
        self.assertEqual(len(response["data"]["users"]["nodes"]), 1)

    @patch("linear_python.base.requests.post")
    def test_get_viewer(self, mock_post):
        # Setup mock response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "data": {
                "viewer": {
                    "id": "viewer1",
                    "name": "Current User",
                    "email": "current@example.com",
                }
            }
        }

        # Make request
        response = self.client.get_viewer()

        # Assert request was made with correct parameters
        mock_post.assert_called_once()
        self.assertEqual(response["data"]["viewer"]["id"], "viewer1")


if __name__ == "__main__":
    unittest.main()
