from ast import List
from sqlalchemy.orm import Session
from app.models.food import Food
from models.food import Food
from schemas.food import * 

def calculate_calories():
    total_calories = FoodOut.carb * FoodOut.fat * FoodOut.protein
    return total_calories

def get_all_food(db: Session) -> List[Food]:
    return db.query(FoodOut).all()

def get_food(food: FoodOut, db : Session) -> Food:
    return db.query(FoodOut).filter_by(id)

def create_food(food: FoodCreate, db : Session):
    db.query()

def update_food():
    pass

def get_macros():
    pass

def update_macros():
    pass

def get_calories():
    pass

def delete_food_log():
    pass


