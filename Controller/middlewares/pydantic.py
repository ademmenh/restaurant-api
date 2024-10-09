
from fastapi import HTTPException
from pydantic import BaseModel, validator
from ..schemas.enums import EnumMeals



GENRE = ('genre1', 'genre2', 'genre3')

class Meal (BaseModel):
    id : int
    name : str
    genre : EnumMeals





class POSTMeal (BaseModel):

    name : str
    genre : str


    @validator ('name')
    def check_name (cls, name):
        return name.title()


    @validator ('genre')
    def check_genre (cls, genre):
        genre = genre.lower()
        if genre not in GENRE:
            raise HTTPException (status_code=422)
        return genre
