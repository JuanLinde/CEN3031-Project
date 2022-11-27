from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str
    user_email: str
    user_password: str

class LessonBase(BaseModel):
    lesson_name: str
    lesson_type: str
    lesson_language: str

class FlashcardBase(BaseModel):
    lesson_name: str
    flashcard_content: str