
from sqlmodel import create_engine, Session
from sqlmodel import SQLModel, Field, select





def engine ():
    return create_engine('sqlite:///project1/Model/orm.sqlite', echo=True)

def create_tables (engine):
    SQLModel.metadata.create_all(engine)



class Meal (SQLModel, table=True):
    id : int = Field (primary_key=True)
    name : str = Field ( max_length=15)
    genre : str = Field (max_length=10)
