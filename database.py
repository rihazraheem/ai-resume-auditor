from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from config import Config

Base=declarative_base()
engine=create_engine(Config.DB_URL)
Session=sessionmaker(bind=engine)

class Candidate(Base):
    __tablename__='candidates'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    email=Column(String)
    phone_number = Column(String)
    file_name = Column(String)
    score=Column(Float)
    status=Column(String)

Base.metadata.create_all(engine)

def save_entry(name, email, phone, filename, score):
    session=Session()
    status="Pass" if score >= Config.MATCH_THRESHOLD else "Fail"
    new_c=Candidate(name=name, email=email, phone_number=phone, file_name=filename, score=score, status=status)
    session.add(new_c)
    session.commit()
    session.close()

def get_df():
    with engine.connect() as conn:
      return pd.read_sql("SELECT * FROM candidates", engine)
