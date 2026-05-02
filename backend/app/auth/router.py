from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from fastapi import APIRouter, HTTPException
from app.auth.schemas import UserCreate, UserLogin
from app.auth.service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(data: UserCreate):
    try:
        return register_user(data.email, data.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(data: UserLogin):
    try:
        return login_user(data.email, data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    
@router.post("/token")
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        return login_user(form_data.username, form_data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))