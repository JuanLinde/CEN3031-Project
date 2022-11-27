from sqlalchemy.orm.session import Session
from database.models import DbFlashcard, DbLesson
from schemas import FlashcardBase, LessonBase, UserBase
from database.models import DbUser, DbLesson, DbFlashcard

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        user_name = request.user_name,
        user_email = request.user_email,
        user_password = request.user_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_lesson(db: Session, request: LessonBase):
    new_lesson = DbLesson(
        lesson_name = request.lesson_name,
        lesson_type = request.lesson_type,
        lesson_language = request.lesson_language
    )
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)
    return new_lesson

def create_flashcard(db: Session, request: FlashcardBase):
    new_flashcard = DbFlashcard(
        lesson_name = request.lesson_name,
        flashcard_content = request.flashcard_content
    )
    db.add(new_flashcard)
    db.commit()
    db.refresh(new_flashcard)
    return new_flashcard

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_all_lessons(db: Session):
    return db.query(DbLesson).all()

def get_all_flashcards(db: Session):
    return db.query(DbFlashcard).all()

def get_user_by_id(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.user_id == id).first()

def get_lesson_by_id(db: Session, id: int):
    return db.query(DbLesson).filter(DbLesson.lesson_id == id).first()

def get_flashcard_by_id(db: Session, id: int):
    return db.query(DbFlashcard).filter(DbFlashcard.flashcard_id == id).first()