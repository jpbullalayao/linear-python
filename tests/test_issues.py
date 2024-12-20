import pytest

from linear_python.resources.issues import IssueClient


@pytest.fixture
def issue_client():
    return IssueClient("test_api_key")


def test_create_issue_success(issue_client, mocker):
    mock_response = {
        "data": {
            "issueCreate": {
                "success": True,
                "issue": {
                    "id": "test-id",
                    "title": "Test Issue",
                    "url": "http://linear.app/issue/TEST-1",
                },
            }
        }
    }
    mocker.patch.object(issue_client, "_make_request", return_value=mock_response)

    result = issue_client.create_issue(
        {"team_id": "team-1", "title": "Test Issue", "description": "Test Description"}
    )

    assert result == mock_response["data"]["issueCreate"]


def test_create_issue_validation(issue_client):
    with pytest.raises(TypeError):
        issue_client.create_issue("not a dict")

    with pytest.raises(ValueError):
        issue_client.create_issue({})

    with pytest.raises(ValueError):
        issue_client.create_issue({"team_id": "team-1"})


def test_get_issue(issue_client, mocker):
    mock_response = {"data": {"issue": {"id": "test-id", "title": "Test Issue"}}}
    mocker.patch.object(issue_client, "_make_request", return_value=mock_response)

    result = issue_client.get_issue("test-id")
    assert result == mock_response["data"]["issue"]


def test_update_issue(issue_client, mocker):
    mock_response = {
        "data": {
            "issueUpdate": {
                "success": True,
                "issue": {"id": "test-id", "title": "Updated Title"},
            }
        }
    }
    mocker.patch.object(issue_client, "_make_request", return_value=mock_response)

    result = issue_client.update_issue("test-id", {"title": "Updated Title"})
    assert result == mock_response["data"]["issueUpdate"]


def test_delete_issue(issue_client, mocker):
    mock_response = {"data": {"issueDelete": {"success": True}}}
    mocker.patch.object(issue_client, "_make_request", return_value=mock_response)

    result = issue_client.delete_issue("test-id")
    assert result == mock_response["data"]["issueDelete"]
