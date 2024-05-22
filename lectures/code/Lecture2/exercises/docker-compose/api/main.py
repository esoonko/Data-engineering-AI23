# api/main.py
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import os

app = FastAPI()

DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    id = Column(String, primary_key=True)
    name = Column(String, index=True)
    country = Column(String)

Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    df = pd.read_csv('https://drive.google.com/uc?id=1zO8ekHWx9U7mrbx_0Hoxxu6od7uxJqWw&export=download')
    with SessionLocal() as session:
        for index, row in df.iterrows():
            data = Data(
                id=row['Customer Id'],
                name=row['First Name'],
                country=row['Country']
                )
            session.add(data)
        session.commit()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data/")
def read_data(skip: int = 0, limit: int = 10):
    with SessionLocal() as session:
        data = session.query(Data).offset(skip).limit(limit).all()
        return data
