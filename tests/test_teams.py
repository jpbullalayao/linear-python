import pytest

from linear_python.resources.teams import TeamClient


@pytest.fixture
def team_client():
    return TeamClient("test_api_key")


def test_get_teams(team_client, mocker):
    mock_response = {
        "data": {
            "teams": {
                "nodes": [
                    {"id": "team-1", "name": "Team 1"},
                    {"id": "team-2", "name": "Team 2"},
                ]
            }
        }
    }
    mocker.patch.object(team_client, "_make_request", return_value=mock_response)

    result = team_client.get_teams()
    assert result == mock_response


def test_get_team(team_client, mocker):
    mock_response = {
        "data": {
            "team": {
                "id": "team-1",
                "name": "Team 1",
                "members": {"nodes": [{"id": "user-1", "name": "User 1"}]},
            }
        }
    }
    mocker.patch.object(team_client, "_make_request", return_value=mock_response)

    result = team_client.get_team("team-1")
    assert result == mock_response
