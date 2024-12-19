from typing import List, Optional
import strawberry


@strawberry.type
class User:
    email: str
    id: strawberry.ID
    isMe: bool
    name: str 
    url: str


@strawberry.type
class UserConnection:
    nodes: List[User]