"""
SQLAlchemy User Model

This module defines an SQLAlchemy User model class for database interactions.

Usage:
1. Import this module to access the `User` model class for database operations.
2. The `User` class represents the "users" table in the database and includes columns for id, username, email, and hashed_password.

Example:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import User

# Create an SQLAlchemy engine and session
engine = create_engine("sqlite:///mydatabase.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Example usage:
new_user = User(username="example_user", email="user@example.com", hashed_password="hashed_password_here")
db.add(new_user)
db.commit()
```

For detailed information on the structure of the User model and how to use it for database operations, refer to the class definition and example usage above.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
