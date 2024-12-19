from typing import Optional

import strawberry


@strawberry.type
class Project:
    id: strawberry.ID
    description: str
    name: str
    url: str


@strawberry.type
class ProjectCreateInput:
    description: Optional[str]
    name: str
    priority: Optional[int]
    state: Optional[str]
    teamIds: list[str]


@strawberry.type
class ProjectPayload:
    project: Optional[Project]
    success: bool
