from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from ..database import Base

class Meal(Base):
    __tablename__ = 'meal'

    id = Column(Integer, primary_key= True, nullable=False)

