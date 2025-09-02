from ast import List
from sqlalchemy.orm import Session
from models.food import Food
from schemas.food import * 

def calculate_calories():
    return total_calories

def get_all_food(db: Session) -> List[Food]:
    return db.query(Food).all()

def get_food(food: Food, db : Session) -> Food:
    return db.query(Food).filter_by(id)

def create_food(food: Food, db : Session):
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


