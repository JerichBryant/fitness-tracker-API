from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from ..database import Base

class Food(Base):
    __tablename__ = 'food'

    food_id = Column(Integer, primary_key= True, nullable= False)
    name = Column(String)
    calories = Column(Integer, nullable=False)
    protein = Column(Float)
    fat = Column(Float)
    carb = Column(Float)
    times_tamp = Column(TIMESTAMP)
    

    



    
