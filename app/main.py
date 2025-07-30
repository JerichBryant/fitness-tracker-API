from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

@app.get("/")
def check_on():
    return {"message" : "Hello world!"}