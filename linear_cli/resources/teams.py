from ..base import BaseClient


class TeamClient(BaseClient):
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

        return self._make_request(query)

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

        return self._make_request(query, variables)
