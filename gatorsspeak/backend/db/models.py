from db.database import base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String 

# This is where we provide the tables' information

class Db_Test(base):
    __tablename__ = 'test_table'
    # This cretes the test_id column. The index attribute autocreates a new id
    # for each record that is created in the table.
    test_id = Column(Integer, primary_key=True, index=True)
    # This creates a test_string column.
    test_string_col = Column(String)