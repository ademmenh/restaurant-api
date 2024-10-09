
from fastapi import HTTPException
from pydantic import BaseModel, validator



GENRE = ('Genre1', 'Genre2', 'Genre3')


class Meal (BaseModel):
    id : int
    name : str
    genre : str





class GETMeal (BaseModel):

    name : str | None = None
    genre : str | None = None



    @validator ('name')
    def check_name (cls, name):
        return name.title()

    @validator ('genre')
    def chack_genre (cls, genre):
        return genre.title()
         




class POSTMeal (BaseModel):

    name : str
    genre : str


    @validator ('name')
    def check_name (cls, name):
        return name.title()


    @validator ('genre')
    def check_genre (cls, genre):
        genre = genre.title()
        if genre not in GENRE:
            raise HTTPException (status_code=422)
        return genre
