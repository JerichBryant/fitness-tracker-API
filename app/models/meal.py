from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from ..database import Base



class Meal(Base):
    __tablename__ = 'meal'

    meal_id = mapped_column(Integer, primary_key= True, nullable=False)
    type_meal = Column(String, nullable = False)
    time_stamp = Column(TIMESTAMP)
     




