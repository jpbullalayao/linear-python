from ..base import BaseClient

from ..types import Issue, IssueArchivePayload, IssueCreateInput, IssuePayload, IssueUpdateInput

class IssueClient(BaseClient):
    def create_issue(self, data: IssueCreateInput) -> IssuePayload:
        """
        Create an issue using a dictionary of issue data.
        Required fields: team_id, title
        Optional fields: description, priority, status
        """
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        if "team_id" not in data:
            raise ValueError("team_id is required in data")

        if "title" not in data:
            raise ValueError("title is required in data")

        # Convert team_id to teamId for GraphQL API
        api_data = {
            "input": {
                "teamId": data.pop("team_id"),
                **data
            }
        }

        mutation = """
        mutation CreateIssue($input: IssueCreateInput!) {
            issueCreate(
                input: $input
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

    def get_issue(self, issue_id) -> Issue:
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


    def update_issue(self, issue_id: str, data: IssueUpdateInput = None) -> IssuePayload:
        """
        Update an issue using a dictionary of field data.
        Required fields: issue_id
        Optional fields in data dict: title, description
        """
        if data is not None and not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        mutation = """
        mutation UpdateIssue($issueId: String!, $input: IssueUpdateInput!) {
            issueUpdate(
                id: $issueId,
                input: $input
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

        api_data = {
            "input": {
                "issueId": issue_id,
                **(data or {})
            }
        }
        return self._make_request(mutation, api_data)

    def delete_issue(self, issue_id, permanently_delete=True) -> IssueArchivePayload:
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

        api_data = {
            "issueId": issue_id,
            "permanentlyDelete": permanently_delete,
        }

        return self._make_request(mutation, api_data)

