from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.schemas import UserCreate, UserLogin
from app.auth.service import login_user, register_user
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, data.email, data.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    try:
        return login_user(db, data.email, data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/token")
def token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    try:
        return login_user(db, form_data.username, form_data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))