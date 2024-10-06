
from fastapi import FastAPI
from fastapi import HTTPException

from .schemas.enums import EnumMeals
from .schemas.data import MEALS

from .middlewares.validation import Meal



app = FastAPI()








@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}





@app.get ('/meals')

async def Meals ( name: str|None = None, genre: EnumMeals|None = None) -> list[Meal] :
    vlMeals = [Meal(**meal) for meal in MEALS]
    if name:
        vlMeals = [meal for meal in vlMeals if meal.name==name]
    if genre:
        vlMeals = [meal for meal in vlMeals if meal.genre==genre.value]
    return vlMeals
