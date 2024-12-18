from typing import Optional
import strawberry


@strawberry.type
class Issue:
    id: strawberry.ID
    title: str 
    url: str


@strawberry.type
class IssueArchivePayload:
    entity: Issue
    lastSyncId: float
    success: bool


@strawberry.type
class IssueCreateInput:
    description: Optional[str]
    team_id: str
    title: Optional[str]


@strawberry.type
class IssuePayload:
    issue: Issue
    lastSyncId: float
    success: bool


@strawberry.type
class IssueUpdateInput:
    description: Optional[str]
    title: Optional[str]
