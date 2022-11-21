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

# Read all data in test table
@router.get('/')
def get_all_data_in_test_table(db: Session = Depends(get_db)):
    return db_test.read_all_data_from_test_table(db)

# Read data by id
@router.get('/{id}')
def get_test_table_data_by_id(id:int, db: Session = Depends(get_db)):
    return db_test.read_data_from_test_table_by_id(db, id)

# Read data from test table

# Update data from test table

# Delete data from test table