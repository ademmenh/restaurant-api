
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from .schemas.enums import EnumMeals
from .middlewares.pydantic import Meal, POSTMeal


from ..Model.data import MEALS
from ..Model import schemas
from ..Model import connection



@asynccontextmanager
async def lifespan (app: FastAPI):
    connection.init()
    yield



app = FastAPI(lifespan=lifespan)








@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}





@app.get ('/meals')
async def meals ( name: str|None = None, genre: EnumMeals|None = None) -> list[Meal] :
    vlMeals = MEALS.copy()
    if name:
        vlMeals = [meal for meal in vlMeals if meal['name']==name]
    if genre:
        vlMeals = [meal for meal in vlMeals if meal['genre']==genre.value]
    return vlMeals





# @app.post ('/meals')
# async def meals_ ( aname: str, agenre: EnumMeals) -> None:
#     aid = MEALS[-1]['id'] + 1

#     meal = {'id':aid, 'name':aname, 'genre':agenre.value}
#     MEALS.append (meal)

@app.post ('/meals')
async def meals_ ( meal : POSTMeal ) -> None:
    viid = MEALS[-1]['id'] + 1

    meal = {'id':viid, 'name':meal.name, 'genre':meal.genre.value}
    MEALS.append (meal)

