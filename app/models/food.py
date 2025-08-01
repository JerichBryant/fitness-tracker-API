from logging import fatal
from sqlalchemy import TIMESTAMP, Column, Float, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from ..database import Base

class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key= True, nullable= False)
    calories = Column(Integer)
    protein = Column(Float)
    fat = Column(Float)
    carb = Column(Float)

    
