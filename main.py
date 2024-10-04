
from fastapi import FastAPI



app = FastAPI()

@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}




MEALS =\
[
    {'id':1, 'name':'meal1'},
    {'id':2, 'name':'meal2'},
    {'id':3, 'name':'meal3'},
]

@app.get ('/meals')
async def meals () -> list[dict]:
    return MEALS
