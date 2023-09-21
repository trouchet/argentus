from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, services
from app.database import get_db

router = APIRouter()


@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.crud.create_user(db, user)


@router.post("/login")
def login_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return authenticate_user(db, user)


def authenticate_user(db: Session, user: schemas.UserCreate):
    # Implement authentication logic here
    # Verify user credentials, generate JWT, and return it
    pass
