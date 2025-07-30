from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.meal import Meal as MealModel
from schemas.meal import Meal as MealSchema

router = APIRouter()

@router.get("/meals/", tags =["meals"])
async def get_all_meals(db : Session = Depends(get_db)):
    meals = db.query(MealModel).all()
    return meals    