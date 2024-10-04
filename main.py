
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

@app.get ('/meals/{mid}')

async def meals (mid : int|None) -> list[dict] | dict | str:

    if mid is None:
        return MEALS
    elif isinstance (mid, int):
        for dic in MEALS:
            if dic['id']==mid :
                return dic
                break
        return f"the {mid} mid do not exist !"
    else:
        return "the id must be an int"





