from pydantic import BaseModel
    
class Meal(BaseModel):
    name : str
    timestamp : float

class MealCreate(Meal):
    pass

class MealOut(Meal):
    id : int

    class Config:
        orm_mode = True
