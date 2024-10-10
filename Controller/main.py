
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from .middlewares.pydantic import Meal, GETMeal, POSTMeal

from ..Model.data import MEALS
from ..Model import orm





@asynccontextmanager
async def db_lifespan (app: FastAPI):
    orm.create_tables (orm.engine)
    yield


app = FastAPI(lifespan=db_lifespan)





@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}



@app.get ('/meals')
async def meals ( meal:GETMeal ) -> list[Meal]:
    return orm.Meal.get_meal(meal.__dict__)



@app.post ('/meals')
async def meals_ ( meal : POSTMeal ) -> None:
    orm.Meal.post_meal (meal.__dict__)

