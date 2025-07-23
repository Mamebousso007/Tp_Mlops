from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

host = "m2dsia-mlops.cfuik82swe2y.eu-central-1.rds.amazonaws.com"

user = "root"
password = "rootM2dsia"
database = "m2dsia_diarra"

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()