# Linear Python Library

The Linear Python library provides easy integration with the [Linear](https://linear.app/) API from applications built in Python.

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

Create/retrieve your personal Linear API Key in the `Settings & access` tab in the Linear app, and then initialize the python Linear client:

```python
from linear_python import LinearClient
client = LinearClient("lin_api_***")
```

You're now ready to use the Linear client! `linear-python` currently provides 1-to-1 python functions to some GraphQL queries/mutations that you would call to access the Linear API. Below are a few sample functions you can call.

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

### Contributing

There is currently a lot of work to do on this library. A lot of Linear API's GraphQL queries/mutations do not have `linear-python` functions. Feel free to tweet me [@professorragna](https://twitter.com/professorragna) if you're interested in contributing to this library.

## Resources

- [Linear Docs](https://developers.linear.app/docs)

## License

MIT License
