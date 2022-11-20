from pydantic import BaseModel

# This class provides the definition for the information the client will send to
# the database. test_string_col comes from backend/db/models.py This will hold the 
# information passed by the client through the request. The request is handled in backend/db/db_test.py
class TestBase(BaseModel):
    test_string_col: str