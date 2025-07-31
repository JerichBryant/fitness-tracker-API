from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from crud import meal as meal_crud

router = APIRouter()

@router.get("/meals/", tags =["meals"])
async def get_all_meals(db : Session = Depends(get_db)):
    return meal_crud.get_all_meals(db)