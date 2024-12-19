from ..base import BaseClient
from ..types import ProjectCreateInput, ProjectPayload


class ProjectClient(BaseClient):
    def create_project(self, data: ProjectCreateInput) -> ProjectPayload:
        """
        Create a project using a dictionary of project data.
        Required fields: name, teamIds
        Optional fields: description, priority
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        if "name" not in data:
            raise ValueError("name is required in data")

        if "teamIds" not in data:
            raise ValueError("teamIds is required in data")

        mutation = """
        mutation CreateProject($input: ProjectCreateInput!) {
            projectCreate(
                input: $input
            ) {
                  success
                  project {
                      id
                      name
                      url
                  }
              }
          }
        """

        api_data = {"input": {**data}}

        response = self._make_request(mutation, api_data)
        if not response:
            return response

        return response["data"]["projectCreate"]
