from sqlalchemy.orm import Session
from Models.DBEntities import User
from Models.ModelsDto import UserModel


def create_user(db: Session, user: UserModel):
    new_user = serialize_user_model(user)
    # db .add(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def serialize_user_model(user: User.User):
    print(user)
    if user is None:
        return
    serialized_to_dict = dict(user)
    return serialized_to_dict


def get_users(db: Session, skip: int, limit: int):
    return db.query(User.User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, username: str):
    return db.query(User.User).filter(User.login == username).first()
