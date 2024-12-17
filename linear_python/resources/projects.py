from ..base import BaseClient


class ProjectClient(BaseClient):
    def create_project(self, project_data: dict):
        """
        Create a project using a dictionary of project data.
        Required fields: name, teamIds
        Optional fields: description, priority
        """
        if not isinstance(project_data, dict):
            raise TypeError("project_data must be a dictionary")

        if "name" not in project_data:
            raise ValueError("name is required in project_data")

        if "teamIds" not in project_data:
            raise ValueError("teamIds is required in project_data")

        mutation = """
        mutation CreateProject($name: String!, $description: String, $priority: Int, $teamIds: [String!]!) {
            projectCreate(
                input: {
                    name: $name,
                    description: $description,
                    priority: $priority,
                    teamIds: $teamIds
                }
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

        return self._make_request(mutation, project_data)
