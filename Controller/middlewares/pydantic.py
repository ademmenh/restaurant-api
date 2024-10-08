
from pydantic import BaseModel
from ..schemas.enums import EnumMeals

class Meal (BaseModel):
    id : int
    name : str
    genre : str

class POSTMeal (BaseModel):
    name : str
    genre : EnumMeals
