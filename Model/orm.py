
from sqlmodel import create_engine, Session
from sqlmodel import SQLModel, Field, select





engine = create_engine('sqlite:///project1/Model/orm.sqlite', echo=True)

def create_tables (engine):
    SQLModel.metadata.create_all(engine)



class Meal (SQLModel, table=True):
    
    id : int = Field (primary_key=True)
    name : str = Field ( max_length=15)
    genre : str = Field (max_length=10)


    
    def get_meal (**kwargs):
        filters = []
        for key, value in kwargs.items():
            if key is not None:
                filters.append(key==value)

        with Session(engine) as session:
            result = session.exec(select(Meal).where(*filters)).all()
            return result
