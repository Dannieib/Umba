from typing import List
import uvicorn
from fastapi import Depends
from sqlalchemy.orm import Session
from Infrastructure.Database.UserDatabase import SessionLocal
from Models.ModelsDto.UserModel import UserModel
from Services.logics import UserService
import fastapi

router = fastapi.FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/api/v1/get_user')
async def process_github_users(db: Session = Depends(get_db)):
    resp = await UserService.process_github_users(db=db)
    print(resp)
    return resp


@router.get("/api/v1/get_all_users", response_model=List[UserModel])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = UserService.read_users(skip=skip, limit=limit, db=db)
    return users


uvicorn.run(router)
