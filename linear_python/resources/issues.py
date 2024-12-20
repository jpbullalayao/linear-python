from ..base import BaseClient
from ..types import (
    Issue,
    IssueArchivePayload,
    IssueCreateInput,
    IssuePayload,
    IssueUpdateInput,
)


class IssueClient(BaseClient):
    def create_issue(self, data: IssueCreateInput) -> IssuePayload:
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        if "teamId" not in data:
            raise ValueError("teamId is required in data")

        if "title" not in data:
            raise ValueError("title is required in data")

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

        api_data = {"input": {**data}}

        response = self._make_request(mutation, api_data)
        if not response:
            return response

        return response["data"]["issueCreate"]

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

        response = self._make_request(query, variables)
        if not response:
            return response

        return response["data"]["issue"]

    def update_issue(
        self, issue_id: str, data: IssueUpdateInput = None
    ) -> IssuePayload:
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

        api_data = {"issueId": issue_id, "input": {**(data or {})}}

        response = self._make_request(mutation, api_data)
        if not response:
            return response

        return response["data"]["issueUpdate"]

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
            # "permanentlyDelete": permanently_delete,
        }

        response = self._make_request(mutation, api_data)
        if not response:
            return response

        return response["data"]["issueDelete"]
