from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import TestBase
from db.database import get_db
from db import db_test

# This module handles the routing when the API gets hit. 

router = APIRouter(
    prefix='/test',
    tags=['test']
)

# Insert data to test table
@router.post('/')
def instert_data_to_test_table(request:TestBase, db: Session = Depends(get_db)):
    return db_test.insert_to_test_table(db, request)


# Read data from test table

# Update data from test table

# Delete data from test table