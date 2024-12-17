# Linear Python

A Python client for the Linear API.

## Installation

```bash
pip install linear-python
```

## Usage

### Configuration

Create an `.env` file that contains your personal Linear API Key:

```
LINEAR_API_KEY=your-api-key
```

Then, you are ready to initialize the python Linear client

```python
from linear_python import LinearClient, Config
client = LinearClient(Config.API_KEY)
```

### Get Current User (Viewer)

```python
viewer = client.get_viewer()
print(f"Current user: {viewer['data']['viewer']['name']}")
```

### Create an Issue

```python
issue_data = {
    "team_id": "your-team-id",
    "title": "New bug report",
    "description": "Description of the issue"
}
new_issue = client.create_issue(issue_data)
print(f"Created issue: {new_issue['data']['issueCreate']['issue']['url']}")
```

## Resources

- [Linear Docs](https://developers.linear.app/docs)

## License

MIT License
