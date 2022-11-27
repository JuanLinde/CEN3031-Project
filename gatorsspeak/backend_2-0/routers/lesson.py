from fastapi import APIRouter, Depends
from schemas import LessonBase
from sqlalchemy.orm import Session
from database.database import get_db
from database import tables_functionalities

lesson_router = APIRouter(
    prefix='/lesson',
    tags=['lesson']
)

@lesson_router.post('/')
def create_lesson(request: LessonBase, db: Session = Depends(get_db)):
    return tables_functionalities.create_lesson(db, request)

@lesson_router.get('/')
def get_all_lessons(db:Session = Depends(get_db)):
    return tables_functionalities.get_all_lessons(db)

@lesson_router.get('/{id}')
def get_lesson_by_id(id:int, db: Session = Depends(get_db)):
    return tables_functionalities.get_lesson_by_id(db, id)