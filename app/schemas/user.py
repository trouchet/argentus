"""
Pydantic User Schemas

This module defines Pydantic schemas for working with user data. It includes schemas for creating and retrieving user information.

Usage:
1. Import this module to access the `UserBase`, `UserCreate`, and `User` Pydantic schemas for user data validation and serialization.
2. These schemas are used to validate and serialize data for user creation, retrieval, and other user-related operations.

Example:
```python
from app.schemas import UserBase, UserCreate, User

# Validate user data before creating a new user
new_user_data = UserCreate(username="example_user", email="user@example.com", password="password123")
new_user = User(**new_user_data.dict())

# Serialize a user object to JSON for API responses
user = User(id=1, username="example_user", email="user@example.com")
user_json = user.json()
"""

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
