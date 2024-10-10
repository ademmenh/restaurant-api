
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from .middlewares.pydantic import Meal, GETMeal, POSTMeal

from ..Model.data import MEALS
from ..Model import orm





@asynccontextmanager
async def db_lifespan (app: FastAPI):
    engine = orm.engine ()
    orm.create_tables (engine)
    yield


app = FastAPI(lifespan=db_lifespan)





@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}



@app.get ('/meals')
async def meals ( meal:GETMeal ) -> list[Meal] :
    vlMeals = MEALS.copy()
    if meal.name:
        vlMeals = [vdMeal for vdMeal in vlMeals if vdMeal['name']==meal.name]
    if meal.genre:
        vlMeals = [vdMeal for vdMeal in vlMeals if vdMeal['genre']==meal.genre]
    return vlMeals



@app.post ('/meals')
async def meals_ ( meal : POSTMeal ) -> None:
    viid = MEALS[-1]['id'] + 1

    meal = {'id':viid, 'name':meal.name, 'genre':meal.genre}
    print (meal)
    MEALS.append (meal)

