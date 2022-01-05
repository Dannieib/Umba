from pydantic import BaseModel
from Infrastructure.Database.UserDatabase import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    id = Column(Integer)
    login = Column(String)
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
    site_admin = Column(Boolean, default=False)
