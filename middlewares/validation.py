
from pydantic import BaseModel

class Meal (BaseModel):
    id : int
    name : str
    genre : str
