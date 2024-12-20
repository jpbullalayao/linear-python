# Linear Python

A Python client for the [Linear](https://linear.app/) API.

## Requirements

- Python 3.7+
- Required packages (automatically installed):
  - requests
  - python-dotenv
  - strawberry-graphql
  - pydantic
  - typing-extensions

## Installation

The package and all its dependencies can be installed via pip:

```bash
pip install linear-python
```

## Usage

### Configuration

Retrieve your personal Linear API Key, and then initialize the python Linear client:

```python
from linear_python import LinearClient
client = LinearClient("<Linear API Key Here>")
```

You're now ready to use linear-python! Below are a few sample functions you can call.

#### Get Current User (Viewer)

```python
viewer = client.get_viewer()
```

#### Create an Issue

```python
issue_data = {
    "teamId": "your-team-id",
    "title": "New bug report",
    "description": "Description of the issue"
}
new_issue = client.create_issue(issue_data)
```

## Resources

- [Linear Docs](https://developers.linear.app/docs)

## License

MIT License
