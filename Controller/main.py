
from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager

from .middlewares.pydantic import Meal, GETMeal, POSTMeal

from ..Model import orm

from fastapi.security import OAuth2PasswordBearer




@asynccontextmanager
async def db_lifespan (app: FastAPI):
    orm.create_tables (orm.engine)
    yield





app = FastAPI(lifespan=db_lifespan)



@app.get ('/home')
async def home () -> dict [str, str]:
    return {"home":"this is home"}



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get ('/auth')
async def auth (token=Depends(oauth2_scheme)):
    return token



@app.get ('/meals')
async def meals ( meal:GETMeal ) -> list[Meal]:
    return orm.Meal.get_meal(meal.__dict__)



@app.post ('/meals')
async def meals_ ( meal : POSTMeal ) -> None:
    orm.Meal.post_meal (meal.__dict__)

