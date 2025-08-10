from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

# Pydantic model for Post data validation

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):   # Response Modal
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# Inherit from PostBase
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id : int
    owner: UserOut

    class Config:
        orm_mode = True # Enable ORM mode to read data from ORM models  

    
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

# User Schemas

class UserCreate(BaseModel):
    email: EmailStr
    password: str

# User Response Schema


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None  # Optional field, can be None if not provided
    
    class Config:
        orm_mode = True  # Enable ORM mode to read data from ORM models


#  Voting Schemas

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # type: ignore # 1 for like, 0 for dislike


    class Config:
        orm_mode = True  # Enable ORM mode to read data from ORM models