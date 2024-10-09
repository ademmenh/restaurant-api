
from fastapi import HTTPException
from pydantic import BaseModel, validator
from ..schemas.enums import EnumMeals



GENRE = ('Genre1', 'Genre2', 'Genre3')

class GETMeal (BaseModel):
    name : str
    genre : str

    @validator ('name')
    def check_name (cls, name):
        if name:
            name = name.title()
        return name

    @validator ('genre')
    def chack_genre (cls, genre):
        if genre:
            genre = genre.title ()
        return genre
            




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
