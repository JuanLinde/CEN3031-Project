from database.database import Base
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column

class DbUser(Base):

    __tablename__ = 'user'
    user_id = Column(Integer, primary_key = True, index = True)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    user_progress = Column(String)

class DbLesson(Base):

    __tablename__ = 'lessons'
    lesson_id = Column(Integer, primary_key = True, index = True)
    lesson_name = Column(String)
    lesson_type = Column(String)
    lesson_language = Column(String)

class DbFlashcard(Base):

    __tablename__ = 'flashcard'
    flashcard_id = Column(Integer, primary_key = True, index = True)
    lesson_name = Column(String)
    flashcard_content = Column(String)
