from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create database engine
engine = create_engine('sqlte:///todo.db')
#create declarative base meta engine insanece
Base = declarative_base()
#Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
