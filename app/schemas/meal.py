from pydantic import BaseModel

class Calories(BaseModel):
    protein : float
    carb : float
    fat : float
    
class Meal(BaseModel):
    name : str
    calories : Calories
    timestamp : float