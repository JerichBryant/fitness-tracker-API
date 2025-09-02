from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from .models import food, meal
from .database import engine, get_db


food.Base.metadata.create_all(bind=engine)
meal.Base.metadata.create_all(bind=engine)

app = FastAPI() 

@app.get("/")
def check_on():
    return {"message" : "Hello world!"}