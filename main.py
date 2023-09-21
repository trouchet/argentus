from fastapi import FastAPI
from app.routers import auth
from app.database import init_db

app = FastAPI()

# Initialize database
init_db()

# Include routers
app.include_router(auth.router)
