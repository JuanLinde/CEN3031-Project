import re
from fastapi import APIRouter, Depends
from schemas import UserBase
from sqlalchemy.orm import Session
from database.database import get_db
from database import tables_functionalities

user_router = APIRouter(
    prefix='/user',
    tags=['user']
)

@user_router.post('/')
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return tables_functionalities.create_user(db, request)

@user_router.get('/')
def get_all_users(db:Session = Depends(get_db)):
    return tables_functionalities.get_all_users(db)

@user_router.get('/{id}')
def get_user_by_id(id:int, db: Session = Depends(get_db)):
    return tables_functionalities.get_user_by_id(db, id)

