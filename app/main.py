from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.database import engine
from app.routers import auth, users, posts  # Import your routers here

models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

@app.get("/")
def check_on():
    return {"message" : "Hello world!"}