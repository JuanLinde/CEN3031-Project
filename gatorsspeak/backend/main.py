from fastapi import FastAPI
from db import models
from db.database import engine
from router import test

# This is needed to start all the processes
app = FastAPI()
# This exposes the functionality to handle requests
app.include_router(test.router)
# This is responsible for the creation of the database when app is started
models.base.metadata.create_all(engine)