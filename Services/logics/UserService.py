from sqlalchemy.orm import Session
from Infrastructure.Repo import UserRepo
from Models.ModelsDto import UserModel
from Services.httpservices import HttpServiceHelper


async def process_github_users(db: Session):
    data = await HttpServiceHelper.get_github_users()
    if data is None:
        return

    # save here to sqlite....
    for user in data:
        insert = create_users(user, db)
        if insert:
            return True
        return


def create_users(user: UserModel.UserModel, db: Session):
    if user:
        # check_for_existing_user = UserRepo.get_user_by_email(db=db, email=user.login)
        # if check_for_existing_user is None:
        u = dict(user)
        insert = UserRepo.create_user(db, u)
        if insert:
            return insert


def read_users(skip: int, limit: int, db: Session):
    users = UserRepo.get_users(db=db, skip=skip, limit=limit)
    return users
