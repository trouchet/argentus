"""
Authentication and Token Utilities

This module defines various utilities for authentication and token handling, including password hashing, access token generation, and user verification.

Usage:
1. Import this module to access the authentication and token-related functions.
2. These utilities are used for tasks like password hashing, generating access tokens, verifying passwords, and extracting user information from tokens.

Example:
```python
from app.auth import create_access_token, verify_password, get_password_hash

# Create an access token with user data
user_data = {"username": "example_user", "email": "user@example.com"}
access_token = create_access_token(user_data)

# Verify a password against a hashed password
hashed_password = get_password_hash("password123")
is_valid = verify_password("password123", hashed_password)
"""

from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import Depends

from decouple import config

DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES = 15

# Load configuration variables from the .env file
SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "ACCESS_TOKEN_EXPIRE_MINUTES", default=DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES, cast=int
)

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()

    expire_increment = (
        expires_delta
        if expires_delta
        else timedelta(minutes=DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    expire = datetime.utcnow() + expire_increment

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return crypt_context.hash(password)


def get_token():
    # Implement token extraction here
    pass


def get_current_user(token: str = Depends(get_token)):
    # Implement token verification here and return user data
    pass
