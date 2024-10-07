
from sqlModel import SQLModel, Field

class Meal (SQLModel, table=True):
    id: int = Field (primary_key=True, default=None)
    name: str
    genre: str
