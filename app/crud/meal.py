from sqlalchemy.orm import Session
from models.meal import Meal
from schemas.meal import MealCreate

def get_all_meals(db : Session) -> list[Meal]:
    return  db.query(MealCreate).all()

def get_meal(db : Session) -> Meal:
    pass

def update_meal(db : Session):
    pass

def delete_meal(db : Session):
    pass

