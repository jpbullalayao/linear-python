import requests


class LinearClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.linear.app/graphql"
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json",
        }

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

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json={"query": mutation, "variables": project_data},
        )

        # Add debugging information
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code != 200:
            return None

        return response.json()

    def create_issue(self, issue_data: dict):
        """
        Create an issue using a dictionary of issue data.
        Required fields: team_id, title
        Optional fields: description, priority, status
        """
        if not isinstance(issue_data, dict):
            raise TypeError("issue_data must be a dictionary")

        if "team_id" not in issue_data:
            raise ValueError("team_id is required in issue_data")

        if "title" not in issue_data:
            raise ValueError("title is required in issue_data")

        # Convert team_id to teamId for GraphQL API
        api_data = {"teamId": issue_data.pop("team_id"), **issue_data}

        mutation = """
        mutation CreateIssue($teamId: String!, $title: String!, $description: String, $priority: Int) {
            issueCreate(
                input: {
                    teamId: $teamId,
                    title: $title,
                    description: $description,
                    priority: $priority
                }
            ) {
                success
                issue {
                    id
                    title
                    url
                }
            }
        }
        """

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json={"query": mutation, "variables": api_data},
        )

        # Add debugging information
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code != 200:
            return None

        return response.json()

    def get_issue(self, issue_id):
        query = """
        query GetIssue($issueId: String!) {
            issue(id: $issueId) {
                id
                assignee {
                  id
                  name
                }
                creator {
                  id
                  name
                }
                description
                dueDate
                labels {
                  nodes {
                    id
                    name
                  }
                }
                priority
                priorityLabel
                project {
                  id
                  name
                }
                state {
                  id
                  name
                  position
                }
                title
                url
            }
        }
        """

        variables = {
            "issueId": issue_id,
        }

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json={"query": query, "variables": variables},
        )

        # Add debugging information
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code != 200:
            return None

        return response.json()

    def update_issue(self, issue_id: str, updates: dict = None):
        """
        Update an issue using a dictionary of field updates.
        Required fields: issue_id
        Optional fields in updates dict: title, description
        """
        if updates is not None and not isinstance(updates, dict):
            raise TypeError("updates must be a dictionary")

        mutation = """
        mutation UpdateIssue($issueId: String!, $title: String, $description: String) {
            issueUpdate(
                id: $issueId,
                input: {
                    title: $title,
                    description: $description
                }
            ) {
                success
                issue {
                    id
                    title
                    description
                }
            }
        }
        """

        variables = {"issueId": issue_id, **(updates or {})}

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json={"query": mutation, "variables": variables},
        )

        # Add debugging information
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code != 200:
            return None

        return response.json()

    def delete_issue(self, issue_id, permanently_delete=True):
        mutation = """
        mutation DeleteIssue($issueId: String!, $permanentlyDelete: Boolean) {
            issueDelete(
                id: $issueId,
                permanentlyDelete: $permanentlyDelete
            ) {
                success
                lastSyncId
                entity {
                    id
                    title
                    description
                }
            }  
        }
        """

        variables = {
            "issueId": issue_id,
            "permanentlyDelete": permanently_delete,
        }

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json={"query": mutation, "variables": variables},
        )

        # Add debugging information
        print(f"Response: {response.json()}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if response.status_code != 200:
            return None

        return response.json()

    def get_me(self):
        query = """
        {
            viewer {
                id
                name
                email
            }
        }
        """
        response = requests.post(
            self.base_url, headers=self.headers, json={"query": query}
        )

        if response.status_code != 200:
            return None

        return response.json()

    def get_teams(self):
        query = """
        {
            teams {
                nodes {
                    id
                    name
                }
            }
        }
        """

        response = requests.post(
            self.base_url, headers=self.headers, json={"query": query}
        )

        if response.status_code != 200:
            return None

        return response.json()

    def get_team(self, team_id):
        query = """
        query GetTeam($teamId: String!) {
            team(id: $teamId) {
                id
                name
                members {
                    nodes {
                        id
                        name
                    }
                }
            }
        }
        """

        variables = {
            "teamId": team_id,
        }

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json={"query": query, "variables": variables},
        )

        # Add debugging information
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code != 200:
            return None

        return response.json()
