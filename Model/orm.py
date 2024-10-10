
from sqlmodel import create_engine, Session
from sqlmodel import SQLModel, Field, select
from sqlalchemy import and_, or_




engine = create_engine('sqlite:///project1/Model/orm.sqlite')

def create_tables (engine):
    SQLModel.metadata.create_all(engine)



class Meal (SQLModel, table=True):
    
    id : int = Field (primary_key=True)
    name : str = Field ( max_length=15)
    genre : str = Field (max_length=10)


    
    def get_meal (dict):
        filters = []
        for key, value in dict.items():
            if value is not None:
                column = getattr(Meal, key)
                filters.append(column==value)

        # print (filters)
        with Session(engine) as session:
            statement = select(Meal).where(and_(*filters))
            # print (statement)
            return session.exec(statement).all()


    def post_meal (dict):
        with Session(engine) as session:
            meal = Meal (**dict)
            session.add_all([meal])
            session.commit()
            session.refresh(meal)

