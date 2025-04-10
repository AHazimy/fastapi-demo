from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import logging
DATABASE_URL = os.environ['DATABASE_URL']

if not DATABASE_URL:
    engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)#, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()