from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app import database, models
from app.config import setting
from . import schemas
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# SECRET_KEY
# Algorithm
# Expiration time

# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=setting.access_token_expire_minutes)
     
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, setting.secret_key, algorithm=setting.algorithm)

    return encoded_jwt

# This function is called by get_current_user
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, setting.secret_key, algorithms=[setting.algorithm])
    
        id: int = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", 
    headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    
    return user

