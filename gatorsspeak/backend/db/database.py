from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# Name of our database
SQLALCHEMY_DATABASE_URL = "sqlite:///./gatorsspeak_db.db"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
 # This is needed to create the database models
base = declarative_base()

# This makes the database available throughout all of the code
def get_db():
    # Anytime there is an operation in the db, it gets the db
    # it yields it, and then closes it without us having to do anything else.
    db = session_local() 
    try:
        yield db
    finally:
        db.close()
