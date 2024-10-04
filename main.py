
from fastapi import FastAPI



app = FastAPI()

@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}




MEALS = \
[
    {'id':777, 'name':'meal1'},
    {'id':19, 'name':'meal2'},
    {'id':28, 'name':'meal3'},
]

@app.get ('/meals')

async def meals () -> list[dict]:
    return MEALS





@app.get ('/meal/{meal_ID}')

async def meal (meal_ID:int) -> dict:
    for dic in  MEALS:
        if dic['id']==meal_ID:
            return dic
            break
            
