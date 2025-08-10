from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from .. import database, models, schemas, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")    
    
    # Create a token
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    
    # Return token
    return {"access_token": access_token, "token_type": "bearer"}

# [User Login Form]
#      ↓
# POST /login → FastAPI
#      ↓
# Validate User + Password
#      ↓
# Generate JWT
#      ↓
# Return Token → Client
#      ↓
# Client stores token
#      ↓
# Every future request:
# Authorization: Bearer <JWT>
#      ↓
# FastAPI verifies JWT
#      ↓
# Access granted ✅
