from linear_cli.base import BaseClient


def test_base_client_initialization():
    client = BaseClient("test_api_key")
    assert client.api_key == "test_api_key"
    assert client.base_url == "https://api.linear.app/graphql"
    assert client.headers == {
        "Authorization": "test_api_key",
        "Content-Type": "application/json",
    }


def test_make_request_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": {"test": "value"}}
    mock_post = mocker.patch("requests.post", return_value=mock_response)

    client = BaseClient("test_api_key")
    result = client._make_request("test_query", {"var": "value"})

    assert result == {"data": {"test": "value"}}
    mock_post.assert_called_once()


def test_make_request_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 400
    mocker.patch("requests.post", return_value=mock_response)

    client = BaseClient("test_api_key")
    result = client._make_request("test_query")

    assert result is None
