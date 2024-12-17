from ..base import BaseClient


class UserClient(BaseClient):
    def get_user(self, user_id: str):
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
        return self._make_request(query, {"id": user_id})

    def get_users(self):
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
        return self._make_request(query)

    def get_viewer(self):
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
        return self._make_request(query)
