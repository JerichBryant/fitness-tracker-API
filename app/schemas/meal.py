from pydantic import BaseModel
    
class Meal(BaseModel):
    name : str
    timestamp : float

    class Config:
        orm_mode= True


