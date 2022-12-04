from fastapi import APIRouter, Depends
from schemas import FlashcardBase
from sqlalchemy.orm import Session
from database.database import get_db
from database import tables_functionalities

flashcard_router = APIRouter(
    prefix = '/flashcard',
    tags=['flashcard']
)

@flashcard_router.post('/')
def create_flashcard(request: FlashcardBase, db: Session = Depends(get_db)):
    return tables_functionalities.create_flashcard(db, request)

@flashcard_router.get('/')
def get_all_flashcards(db:Session = Depends(get_db)):
    return tables_functionalities.get_all_flashcards(db)

@flashcard_router.get('/{id}')
def get_flashcard_by_id(id:int, db: Session = Depends(get_db)):
    return tables_functionalities.get_flashcard_by_id(db, id)