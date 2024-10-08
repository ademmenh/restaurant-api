
from fastapi import FastAPI
from fastapi import HTTPException

from contextlib import asynccontextmanager

from .schemas.enums import EnumMeals
from .middlewares.pydantic import Meal


from ..Model.data import MEALS
from ..Model import schemas
from ..Model import connection



@asynccontextmanager
async def lifespan (app: FastAPI):
    connection.init_db()
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





@app.post ('/meals')
async def meals_ ( aname: str, agenre: EnumMeals) -> None:
    aid = MEALS[-1]['id'] + 1

    meal = {'id':aid, 'name':aname, 'genre':agenre.value}
    MEALS.append (meal)
