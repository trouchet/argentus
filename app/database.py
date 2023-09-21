from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeBase
from sqlalchemy.orm import sessionmaker
import databases
from decouple import config

DATABASE_DIALECT = config('DATABASE_DIALECT')
DATABASE_NAME = config('DATABASE_NAME')
DATABASE_PORT = config('DATABASE_NAME')
DATABASE_USERNAME = config('DATABASE_USERNAME')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')

DATABASE_URL = (
    f'{DATABASE_USERNAME}:{DATABASE_PASSWORD}@db:{DATABASE_PORT}/{DATABASE_NAME}'
)
DATABASE_URI = f'{DATABASE_DIALECT}://{DATABASE_URL}'

# Database engine and session
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database instance
database = databases.Database(DATABASE_URI)

# Base class for declarative models
Base = DeclarativeBase()

# Function to initialize the database


def init_db():
    Base.metadata.create_all(bind=engine)
