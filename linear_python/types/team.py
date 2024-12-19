from typing import List

import strawberry

from .user import UserConnection


@strawberry.type
class Team:
    id: strawberry.ID
    name: str
    members: UserConnection


@strawberry.type
class TeamConnection:
    nodes: List[Team]
