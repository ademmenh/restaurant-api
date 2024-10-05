
from fastapi import FastAPI
from fastapi import HTTPException

from .schemas.enums import *
from .schemas.data import *





app = FastAPI()



@app.get ('/')
async def home () -> dict [str, str]:
    return {"home":"this is home"}





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





@app.get ('/genre/{genre}')
async def genre ( genre:EnumGetGenre ) -> list[dict]:
    return [ x for x in MEALS if x['genre'].lower() == genre.value ]





