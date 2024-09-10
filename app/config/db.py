from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:root@db:3306/assignment", echo=True)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
