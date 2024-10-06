
from fastapi import FastAPI
from fastapi import HTTPException

from .schemas.enums import EnumGetGenre
from .schemas.data import MEALS

from .middlewares.validation import Meal



app = FastAPI()








@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}








@app.get ('/meals')

async def Meals () -> list[Meal] :
    return [ meal for meal in MEALS ]



@app.get ('/meals/mid/')

async def MealMid (mid : int) -> Meal :
    for meal in MEALS:
        if meal['id']==mid :
            return Meal(**meal)
    raise HTTPException (status_code=404, detail=f'the mid {mid} do not exist!')



@app.get ('/meals/genre/{genre}')

async def MealGenre ( genre:EnumGetGenre ) -> list[Meal]:
    return [ Meal(**meal) for meal in MEALS if meal['genre'].lower() == genre.value ]



@app.get ('/meals/name/{name}')

async def MealName ( name:str ) -> Meal:
    for meal in MEALS:
        if meal['name'] == name:
            return Meal(**meal)
            break
    raise HTTPException (status_code=404, detail=f'the meal {name} do not exist !')




