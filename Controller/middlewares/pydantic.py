
from pydantic import BaseModel, validator
from ..schemas.enums import EnumMeals

class Meal (BaseModel):
    id : int
    name : str
    genre : str

class POSTMeal (BaseModel):
    name : str
    genre : EnumMeals

    @validator ('name')
    def check_name (cls, name):
        return name.title()
