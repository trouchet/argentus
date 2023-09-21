"""
Create User Function

This module defines a function for creating a new user in the database using SQLAlchemy.

Usage:
1. Import this module to access the `create_user` function.
2. The `create_user` function takes a SQLAlchemy database session (`db`) and a Pydantic schema (`UserCreate`) for user data.
3. It creates a new user record in the database, commits the transaction, and returns the created user object.

Example:
```python
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

# Create a new user in the database
new_user_data = UserCreate(username="example_user", email="user@example.com", password="password123")
created_user = create_user(db_session, new_user_data)

# The created user object can be used for further operations
print(f"Created user: {created_user.username}, ID: {created_user.id}")
"""

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
