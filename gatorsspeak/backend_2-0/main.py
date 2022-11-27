from fastapi import FastAPI
from database import models
from database.database import engine
from routers import user, lesson, flashcard
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user.user_router)
app.include_router(lesson.lesson_router)
app.include_router(flashcard.flashcard_router)

models.Base.metadata.create_all(engine)

''' 
    This makes sure that the ReactJs app running on localhost:3000 
    is able to make requests to the backend.
'''
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)