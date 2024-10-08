
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = 'sqlite:///db.sqlite'

engine = create_engine (DATABASE_URL, echo=True)

def init ():
    SQLModel.metadata.create_all(engine)

def session ():
    with Session(engine) as session_:
        yield session_