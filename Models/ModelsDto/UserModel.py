from __future__ import annotations

from typing import List

from pydantic import BaseModel


class UserModel(BaseModel):
    user_id: int
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool

    class Config:
        orm_mode = True

    class UserList(BaseModel):
        users: List[UserModel]
