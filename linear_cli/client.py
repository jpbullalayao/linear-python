from .resources.issues import IssueClient
from .resources.projects import ProjectClient
from .resources.teams import TeamClient
from .resources.users import UserClient


class LinearClient:
    def __init__(self, api_key):
        self._issues = IssueClient(api_key)
        self._projects = ProjectClient(api_key)
        self._teams = TeamClient(api_key)
        self._users = UserClient(api_key)

    def __getattr__(self, name):
        # Delegate to appropriate client based on method name
        if hasattr(self._issues, name):
            return getattr(self._issues, name)
        elif hasattr(self._projects, name):
            return getattr(self._projects, name)
        elif hasattr(self._teams, name):
            return getattr(self._teams, name)
        elif hasattr(self._users, name):
            return getattr(self._users, name)
        raise AttributeError(f"'LinearClient' object has no attribute '{name}'")
