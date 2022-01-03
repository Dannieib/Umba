from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String


class User(BaseModel):
    __tablename__ = "GithubUsers"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    node_id = Column(String)
    avatar_url = Column(String)
    gravatar_id = Column(String)
    url = Column(String)
    html_url = Column(String)
    followers_url = Column(String)
    following_url = Column(String)
    gists_url = Column(String)
    starred_url = Column(String)
    subscriptions_url = Column(String)
    organizations_url = Column(String)
    repos_url = Column(String)
    events_url = Column(String)
    received_events_url = Column(String)
    type = Column(String)
    site_admin = Column(Boolean)
