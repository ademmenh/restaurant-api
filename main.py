
from fastapi import FastAPI
from fastapi import HTTPException

from .schemas.enums import *
from .schemas.data import *

from .middlewares.validation import *





app = FastAPI()



@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}





@app.get ('/meals')
async def Meals () -> list[Meal] :
    return [ Meal(**meal) for meal in MEALS ]


@app.get ('/meals/id/{mid}')
async def MealMid (mid : int) -> Meal :
    if isinstance (mid, int):
        for meal in MEALS:
            if meal['id']==mid :
                return meal
                break
        raise HTTPException (status_code=404, detail=f'the mid {mid} do not exist!')
    else:
        raise HTTPException (status_code=404, detail='the mid must be string!')


@app.get ('/meals/genre/{genre}')
async def MealGenre ( genre:EnumGetGenre ) -> list[Meal]:
    return [ Meal(**meal) for meal in MEALS if meal['genre'].lower() == genre.value ]


@app.get ('/meals/name/{name}')
async def MealName ( name:str ) -> Meal:
    for meal in MEALS:
        if meal['name'] == name:
            return meal
            break
    
    raise HTTPException (status_code=404, detail=f'the meal {name} do not exist !')


