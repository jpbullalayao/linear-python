from ..base import BaseClient
from ..types import User, UserConnection


class UserClient(BaseClient):
    def get_user(self, user_id: str) -> User:
        """Get a specific user by ID"""
        query = """
        query GetUser($id: String!) {
            user(id: $id) {
                id
                name
                email
            }
        }
        """

        variables = {"id": user_id}

        response = self._make_request(query, variables)
        if not response:
            return response

        return response["data"]["user"]

    def get_users(self) -> UserConnection:
        """Get all users"""
        query = """
        query GetUsers {
            users {
                nodes {
                    id
                    name
                    email
                }
            }
        }
        """
        response = self._make_request(query)
        if not response:
            return response

        return response["data"]["users"]

    def get_viewer(self) -> User:
        """Get the currently authenticated user"""
        query = """
        query Me {
            viewer {
                id
                name
                email
            }
        }
        """
        response = self._make_request(query)
        if not response:
            return response

        return response["data"]["viewer"]
