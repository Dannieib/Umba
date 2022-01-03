from sqlalchemy.orm import Session
from Models.DBEntities import User


def create_user(db: Session, user: User.User):
    db_user = user  # UserModel.UserModel()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User.User).offset(skip).limit(limit).all()
