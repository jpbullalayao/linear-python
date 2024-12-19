import pytest

from linear_python.resources.projects import ProjectClient


@pytest.fixture
def project_client():
    return ProjectClient("test_api_key")


def test_create_project_success(project_client, mocker):
    mock_response = {
        "data": {
            "projectCreate": {
                "success": True,
                "project": {
                    "id": "test-id",
                    "name": "Test Project",
                    "url": "http://linear.app/project/TEST-1",
                },
            }
        }
    }
    mocker.patch.object(project_client, "_make_request", return_value=mock_response)

    result = project_client.create_project(
        {
            "name": "Test Project",
            "teamIds": ["team-1"],
            "description": "Test Description",
        }
    )

    assert result == mock_response["data"]["projectCreate"]


def test_create_project_validation(project_client):
    with pytest.raises(TypeError):
        project_client.create_project("not a dict")

    with pytest.raises(ValueError):
        project_client.create_project({})

    with pytest.raises(ValueError):
        project_client.create_project({"name": "Test"})
