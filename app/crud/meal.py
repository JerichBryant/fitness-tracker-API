from sqlalchemy.orm import Session
from models.meal import Meal
from schemas.meal import MealCreate

def get_all_meals(db : Session) -> list[Meal]:
    return  db.query(MealCreate).all()
