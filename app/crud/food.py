from ast import List
from sqlalchemy.orm import Session
from app.models.meal import Meal
from models.food import Food
from schemas.food import * 

def calculate_calories():
    total_calories = FoodOut.carb * FoodOut.fat * FoodOut.protein
    return total_calories

def get_all_food(db: Session) -> List[Meal]:
    return db.query(FoodOut).all()

def get_food(db : Session) -> Meal:
    return db.query(FoodOut).filter_by(id)

def create_food(db : Session):
    db.query()

def edit_food():
    pass

def get_macros():
    pass

def get_calories():
    pass

