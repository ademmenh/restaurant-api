
from pydantic import BaseModel

class Meal (BaseModel):
    name : str
    genre : str
