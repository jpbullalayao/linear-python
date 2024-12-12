import requests


class LinearClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.linear.app/graphql"
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json",
        }

    def create_issue(
        self, team_id, title, description=None, priority=None, status=None
    ):
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

        variables = {
            "teamId": team_id,
            "title": title,
            "description": description,
            "priority": priority,
        }

        response = requests.post(
            self.base_url,
            headers=self.headers,
            json={"query": mutation, "variables": variables},
        )

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
