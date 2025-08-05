from sqlalchemy import TIMESTAMP, Column, ForeignKey, ForeignKeyConstraint, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from ..database import Base

class User(Base):
    user_id = Column(Integer, primary_key= True)
    email = Column(String, nullable=False)
    #hashed_password
    is_online = Column(Boolean, nullable = False)