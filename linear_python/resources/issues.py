from ..base import BaseClient


class IssueClient(BaseClient):
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
        return self._make_request(mutation, api_data)

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

        return self._make_request(query, variables)

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
        return self._make_request(mutation, variables)

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

        return self._make_request(mutation, variables)
