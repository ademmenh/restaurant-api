
from fastapi import FastAPI
from fastapi import HTTPException


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
async def meals () -> list[dict] :
    return MEALS





@app.get ('/meals/{mid}')
async def meal (mid : int) -> dict :
    if isinstance (mid, int):
        for dic in MEALS:
            if dic['id']==mid :
                return dic
                break
        raise HTTPException (status_code=404, detail=f'the mid {mid} do not exiet!')
    else:
        raise HTTPException (status_code=404, detail='the mid must be string!')



