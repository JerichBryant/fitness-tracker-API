from pydantic import BaseModel

class Food(BaseModel):
    name : str
    calories : int
    protein : float
    carb : float
    fat : float
    
    class Config:
        orm_mode= True