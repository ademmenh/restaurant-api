
from sqlalchemy import create_engine, create_session
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import select, or_, and_





class User (Base):
    __tablename__ = 'User'
    id          = Column (Integer, primary_key=True)
    name        = Column (String(15))
    lname       = Column (String(15))
    gender      = Column (String(1))
    email       = Column (String(30))
    phone       = Column (String(15))

    def post_user (dict):
        with Session(engine) as session:
            user = User (**dict)
            session.add_all([user])
            session.commit()
            session.refresh(user)




class Meal (Base):
    __tablename__ = 'Meal'
    
    id          = Column (Integer, primary_key=True)
    name        = Column (String(15))
    genre       = Column (String(15), default='Genre3')
    price       = Column (Integer)


    def get_meal (dict):
        filters = []
        for key, value in dict.items():
            if value is not None:
                column = getattr(Meal, key)
                filters.append(column==value)

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



class Purchase (Base):
    userId      = Field (primary_key=True, foreign_key="user.id")
    mealId      = Field (primary_key=True, foreign_key="meal.id")
    user        = Relationship ('User', back_populates='purchase')
    meal        = Relationship ('Meal', back_populates='purchase')

    def post_purchase (dict):
        with Session(engine) as session:
            purchase = Purchase (**dict)
            session.add_all([purchase])
            session.commit()
            session.refresh(purchase)

