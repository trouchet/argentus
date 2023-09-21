"""
FastAPI Application

This module defines a FastAPI application instance and includes a router for authentication endpoints.

Usage:
1. Import this module and run the FastAPI application to start the server.
2. The authentication router is included in the application, providing endpoints for user authentication.
"""

from fastapi import FastAPI
from app.routers.auth import auth_router

app = FastAPI()

app.include_router(auth_router)
