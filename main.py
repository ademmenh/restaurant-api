
from fastapi import FastAPI
from fastapi import HTTPException


app = FastAPI()

@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}




MEALS = \
[
    {'id':777, 'name':'meal1', 'genre':'genre1'},
    {'id':19, 'name':'meal2', 'genre':'genre2'},
    {'id':28, 'name':'meal3', 'genre':'genre3'},
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
        raise HTTPException (status_code=404, detail=f'the mid {mid} do not exist!')
    else:
        raise HTTPException (status_code=404, detail='the mid must be string!')




from enum import Enum
class EnumGetGenre (Enum):
    GENERE1 = 'genre1'
    GENERE2 = 'genere2'
    GENERE3 = 'genere3'


@app.get ('/genre/{genre}')
async def genre ( genre:EnumGetGenre ) -> list[dict]:
    return [ x for x in MEALS if x['genre'].lower() == genre.value ]




