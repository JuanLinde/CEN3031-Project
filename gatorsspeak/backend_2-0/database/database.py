from sqlite3 import dbapi2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-practice.db"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
# This variable is used to create the models in models.py
Base = declarative_base()

# This will allow us to perform operations in the database from anywhere in the code
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()