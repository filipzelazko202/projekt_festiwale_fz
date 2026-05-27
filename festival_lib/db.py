from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_url = "sqlite:///film_festival.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

Base = declarative_base()