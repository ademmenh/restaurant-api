
from sqlmodel import create_engine, Session
from sqlmodel import SQLModel, Field, Relationship,select
from sqlalchemy import and_, or_




engine = create_engine('sqlite:///project1/Model/orm.sqlite')

def create_tables (engine):
    SQLModel.metadata.create_all(engine)



class User (SQLModel, table=True):
    id : int    = Field (primary_key=True)
    name : str  = Field (max_length=15)
    lname : str = Field (max_length=15)
    gender : str = Field (max_length=1)
    email : str = Field (max_length=30)
    phone : str = Field (max_length=15)
    purchase : list["Purchase"] = Relationship(back_populates="user")

    def post_user (dict):
        with Session(engine) as session:
            user = User (**dict)
            session.add_all([user])
            session.commit()
            session.refresh(user)



class Meal (SQLModel, table=True):
    
    id : int    = Field (primary_key=True)
    name : str  = Field (max_length=15, unique=True)
    genre : str = Field (max_length=10, default='Genre3')
    price : int = Field ()
    purchase : list["Purchase"] = Relationship(back_populates="meal")



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



class Purchase (SQLModel, table=True):
    userId : int = Field (primary_key=True, foreign_key="user.id")
    mealId : int = Field (primary_key=True, foreign_key="meal.id")
    user : User  = Relationship (back_populates='purchase')
    meal : Meal  = Relationship (back_populates='purchase')
