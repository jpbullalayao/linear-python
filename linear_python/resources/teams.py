from ..base import BaseClient
from ..types import Team, TeamConnection


class TeamClient(BaseClient):
    def get_teams(self) -> TeamConnection:
        query = """
        query GetTeams {
            teams {
                nodes {
                    id
                    name
                }
            }
        }
        """

        response = self._make_request(query)
        if not response:
            return response

        return response["data"]["teams"]

    def get_team(self, team_id) -> Team:
        query = """
        query GetTeam($teamId: String!) {
            team(id: $teamId) {
                id
                name
                members {
                    nodes {
                        id
                        email
                        name
                    }
                }
            }
        }
        """

        variables = {
            "teamId": team_id,
        }

        response = self._make_request(query, variables)
        if not response:
            return response

        return response["data"]["team"]
